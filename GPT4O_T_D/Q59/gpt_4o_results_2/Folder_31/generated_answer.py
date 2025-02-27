def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    s = str(n)
    while s:
        if not is_prime(int(s)):
            return False
        s = s[1:]
    return True

def all_left_truncatable_prime(numbers):
    if len(numbers) <= 50:
        raise ValueError('The input tuple must contain more than 50 integers.')
    x = numbers[50]
    left_truncatable_primes = [n for n in range(2, x) if left_truncatable_prime(n) and '0' not in str(n)]
    return sorted(left_truncatable_primes, reverse=True)