from sympy import isprime

def all_right_truncatable_prime(tup):
    res = []
    for i in range(2, tup[945]):
        if isprime(i):
            str_i = str(i)
            for j in range(1, len(str_i)):
                if not isprime(int(str_i[:-j])):
                    break
            else:
                res.append(i)
    return sorted(res, reverse=True)