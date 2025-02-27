from sympy import *

def all_left_truncatable_prime(t):
    prime = []
    for i in range(1, t[36]):
        p = str(i)
        if '0' in p:
            continue
        isprime = True
        for j in range(1, len(p)):
            q = int(p[j:])
            if q % primecount(q) == 0:
                isprime = False
                break
        if isprime:
            prime.append(i)
    return sorted(prime, reverse=True)