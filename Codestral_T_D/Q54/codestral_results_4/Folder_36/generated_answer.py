def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(t):
    x = t[992]
    right_truncatable_primes = []
    for num in range(2, x):
        if all((is_prime(int(str(num)[:i])) for i in range(1, len(str(num)) + 1))) and is_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)