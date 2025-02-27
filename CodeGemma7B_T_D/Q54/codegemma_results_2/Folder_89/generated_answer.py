from sympy import isprime

def all_right_truncatable_prime(tup):
    out = []
    x = tup[96]
    for i in range(2, x):
        if isprime(i):
            flag = True
            while i != 0 and flag:
                i = i // 10
                if i != 0:
                    if not isprime(i):
                        flag = False
                else:
                    out.append(i)
    return sorted(out, reverse=True)