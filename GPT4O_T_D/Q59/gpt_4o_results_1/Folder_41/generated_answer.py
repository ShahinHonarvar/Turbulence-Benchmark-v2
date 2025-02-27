def is_prime(n):
    if n in (2, 3):
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def left_truncatable(prime):
    str_prime = str(prime)
    for i in range(len(str_prime)):
        if not is_prime(int(str_prime[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[46]
    left_truncatable_primes = []
    for i in range(2, x):
        if '0' not in str(i) and is_prime(i) and left_truncatable(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)