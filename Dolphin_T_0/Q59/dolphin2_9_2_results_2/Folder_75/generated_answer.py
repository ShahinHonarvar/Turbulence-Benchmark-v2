import sympy

def all_left_truncatable_prime(t):
    x = t[41]
    lltp = []
    for i in range(x):
        if sympy.isprime(i):
            if all((sympy.isprime(int(str(i)[j:])) for j in range(1, len(str(i))))):
                lltp.append(i)
    return sorted(lltp)