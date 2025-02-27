import math

def all_left_right_truncatable_prime(n):
    primes = []
    for prime in range(2, int(math.ceil(math.log(n, 2)) + 1)):
        if str(prime).count('0') == 0:
            while str(prime).count('0') == 0:
                prime = int(str(prime)[1:])
            while str(prime).count('0') == 0:
                prime = int(str(prime)[-1:])
            primes.append(prime)
    return sorted(primes) if primes else []