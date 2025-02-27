import math

def all_right_truncatable_prime(t):
    x = t[30]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            right_truncatable = True
            num = i
            while num > 0:
                if not is_prime(num):
                    right_truncatable = False
                    break
                num //= 10
            if right_truncatable:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True