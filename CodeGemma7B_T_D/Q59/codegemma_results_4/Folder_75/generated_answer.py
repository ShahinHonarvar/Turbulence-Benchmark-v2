from functools import reduce
from sympy.ntheory import isprime

def lefttrunc(x):
    return [int(x[i:]) for i in range(len(x))]

def is_lefttruncatable(x):
    return all((isprime(i) and (not str(i).startswith('0')) for i in lefttrunc(str(x))))

def all_left_truncatable_prime(x):
    return sorted([x for x in range(1, x) if isprime(x) and is_lefttruncatable(x)])