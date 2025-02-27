from sympy import isprime

def all_left_truncatable_prime(t):
    l = []
    for i in range(t[61]):
        k = str(i)
        if '0' not in k and all((isprime(int(j)) for j in [k[i:len(k)] for i in range(1, len(k))])):
            l.append(i)
    return sorted(l)