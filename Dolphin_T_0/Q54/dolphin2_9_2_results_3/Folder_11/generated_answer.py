import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    m = int(math.sqrt(n))
    for x in range(3, m + 1, 2):
        if n % x == 0:
            return False
    return True

def is_truncatable(n):
    s = str(n)
    while s:
        if not is_prime(int(s)):
            return False
        s = s[:-1]
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[86]
    primes = []
    for i in range(2, x):
        if is_prime(i) and is_truncatable(i):
            primes.append(i)
    return sorted(primes)