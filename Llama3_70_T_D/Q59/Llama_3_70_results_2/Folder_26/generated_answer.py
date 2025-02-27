def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[81]
    left_truncatable_primes = []
    for i in range(10, x):
        if '0' not in str(i):
            is_left_truncatable_prime = True
            num_str = str(i)
            for j in range(1, len(num_str)):
                if not is_prime(int(num_str[j:])):
                    is_left_truncatable_prime = False
                    break
            if is_left_truncatable_prime and is_prime(i):
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)