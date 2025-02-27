from sympy import isprime

def all_right_truncatable_prime(a):
    b = []
    for i in range(a[14]):
        if isprime(i) and isprime(int(str(i)[:-1])):
            b.append(i)
    return sorted(b)