from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[29]
    a = []
    for i in range(2, x):
        if isprime(i):
            s = str(i)
            for j in range(len(s) - 1):
                if not isprime(int(s[:-j - 1])):
                    break
            else:
                a.append(i)
    a.sort(reverse=True)
    return a