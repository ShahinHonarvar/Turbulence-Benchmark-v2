def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_truncatable_primes(x):
    primes = []
    candidates = ['2', '3', '5', '7']
    while candidates:
        num_str = candidates.pop()
        num = int(num_str)
        if num < x and is_prime(num):
            primes.append(num)
            for d in '1379':
                new_num_str = num_str + d
                if not any((ch == '0' for ch in new_num_str)):
                    candidates.append(new_num_str)
    return primes

def all_left_truncatable_prime(numbers):
    x = numbers[88]
    primes = generate_truncatable_primes(x)
    return sorted(primes, reverse=True)