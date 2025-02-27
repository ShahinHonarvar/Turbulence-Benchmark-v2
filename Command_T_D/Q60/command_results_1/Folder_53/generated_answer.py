import re

def is_left_right_truncatable_prime(n):
    s = str(n)
    while s and s[0] != '2' and (s[-1] != '0'):
        s = s[1:-1]
    return s == '2' or s == '3'

def all_left_right_truncatable_prime(n):
    if not n:
        return []
    lst = sorted(n)
    for i in range(len(lst)):
        if lst[i] in PRIMES and is_left_right_truncatable_prime(lst[i]):
            yield lst[i]
            break
    for x in range(lst[-1], 3, -1):
        if x in PRIMES and is_left_right_truncatable_prime(x):
            yield x
            break