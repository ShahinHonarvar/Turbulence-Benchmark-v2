import math

def all_left_truncatable_prime(t):

    def check(n):
        while n > 0:
            if n in primes:
                n //= 10
            else:
                return False
        return True

    def is_prime(n):
        if n < 2:
            return False
        if n % 2 == 0 and n > 2:
            return False
        if n % 3 == 0 and n > 3:
            return False
        for i in range(5, int(math.sqrt(n)) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True
    n = t[802]
    primes = [2, 3, 5, 7]
    i = 11
    while i < n:
        if is_prime(i):
            primes.append(i)
        i += 2
    return [i for i in primes if check(i)]