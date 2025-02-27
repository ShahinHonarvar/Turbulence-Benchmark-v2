from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[86]
    rtn = []
    for i in range(1, x):
        if isprime(i):
            s = str(i)
            for j in range(len(s) - 1):
                if not isprime(int(s[j + 1:])):
                    break
            else:
                rtn.append(i)
    return sorted(rtn, reverse=True)