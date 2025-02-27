from sympy import isprime

def truncate_prime(n):
    if isprime(n):
        while n > 10:
            n = int(str(n)[1:])
            if not isprime(n):
                return False
        while n != int(str(n)[0]):
            n = int(str(n)[:-1])
            if not isprime(n):
                return False
        return True
    return False

def all_left_right_truncatable_prime(tup):
    x = tup[54]
    primes = []
    for i in range(2, x + 1):
        if truncate_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)