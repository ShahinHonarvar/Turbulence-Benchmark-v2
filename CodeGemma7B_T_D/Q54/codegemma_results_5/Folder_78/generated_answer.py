from functools import reduce

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

def right_truncatable_prime(n):
    if not is_prime(n):
        return False
    digits = [int(d) for d in str(n)]
    for i in range(len(digits) - 1):
        n = int(str(digits[i:])[:-1])
        if not is_prime(n):
            return False
    return True

def all_right_truncatable_prime(args):
    x = args[23]
    right_truncatable_primes = []
    for n in range(x):
        if right_truncatable_prime(n):
            right_truncatable_primes.append(n)
    return sorted(right_truncatable_primes)