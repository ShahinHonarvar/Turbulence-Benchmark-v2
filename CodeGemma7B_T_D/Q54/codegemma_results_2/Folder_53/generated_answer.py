from sympy import isprime

def all_right_truncatable_prime(tple):
    x = tple[86]
    res = []
    for i in reversed(range(2, x)):
        str_i = str(i)
        if isprime(i):
            for j in range(1, len(str_i)):
                m = int(str_i[:-j])
                if not isprime(m):
                    break
            else:
                res.append(i)
    return sorted(res, reverse=True)