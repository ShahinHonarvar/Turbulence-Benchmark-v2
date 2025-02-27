import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(lst):
    x = lst[39]
    primes = []
    for i in range(x - 1, 0, -1):
        if is_prime(i):
            n = i
            while n != 0:
                if not is_prime(n):
                    break
                n //= 10
            else:
                primes.append(i)
    return sorted(primes, reverse=True)