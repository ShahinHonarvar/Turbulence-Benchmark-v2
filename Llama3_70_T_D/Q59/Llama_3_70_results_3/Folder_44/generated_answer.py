def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[39]
    left_truncatable_primes = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        is_left_truncatable = True
        num_str = str(i)
        for j in range(1, len(num_str)):
            if not is_prime(int(num_str[j:])):
                is_left_truncatable = False
                break
        if is_left_truncatable and is_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)