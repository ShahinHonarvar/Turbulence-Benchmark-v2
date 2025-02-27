from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[630]
    right_trunc = []
    for i in range(2, x):
        if isprime(i) and isprime(int(str(i)[:-1])):
            right_trunc.append(i)
    return sorted(right_trunc, reverse=True)