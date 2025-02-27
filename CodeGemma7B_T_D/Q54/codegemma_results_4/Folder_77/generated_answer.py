from sympy import isprime

def all_right_truncatable_prime(a):
    i = a[767]
    k = []
    for j in range(2, i):
        if isprime(j):
            for l in range(1, len(str(j))):
                if not isprime(j // 10 ** l):
                    break
            else:
                k.append(j)
    return sorted(k, reverse=True)