import math

def right_truncatable_prime(n: int):

    def is_prime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        if n % 2 == 0:
            return False
        sqr = int(math.sqrt(n)) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True
    for i in range(len(str(n)), 0, -1):
        trunc = int(n / 10 ** i)
        if trunc == 0:
            return False
        deleting_digit = n - trunc * 10 ** i
        if deleting_digit != 0 and (not is_prime(deleting_digit)):
            return False
    return True

def all_right_truncatable_prime(x):
    primes = []
    if not is_prime(x):
        return primes
    for i in range(2, x):
        if right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)