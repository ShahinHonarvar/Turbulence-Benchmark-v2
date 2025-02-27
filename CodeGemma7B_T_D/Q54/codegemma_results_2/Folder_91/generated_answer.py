from sympy import *

def all_right_truncatable_prime(x):
    t = []
    for i in range(2, x):
        if isprime(i) and isprime(int(str(i)[:-1])):
            t.append(i)
    t.sort(reverse=True)
    return t