def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(num):
    s = str(num)
    while s:
        if not is_prime(int(s)):
            return False
        s = s[:-1]
    return True

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 28:
        return []
    x = numbers[28]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)