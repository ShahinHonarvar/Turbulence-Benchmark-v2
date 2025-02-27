from sympy import isprime

def all_left_truncatable_prime(j):
    x = j[14]
    i = x % 10 ** (i + 1) == 0 and x % 10 ** i == 0
    z = l = sorted([x % 10 ** i for i in range(len(str(x))) if i and i % 2])
    q = [i for i in z if all([isprime(i) for i in [i // 10 ** j for j in range(len(str(x)) - i)]])]
    return q