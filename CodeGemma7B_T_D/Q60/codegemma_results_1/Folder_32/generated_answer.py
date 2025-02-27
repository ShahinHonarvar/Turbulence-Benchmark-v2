from sympy import isprime

def all_left_right_truncatable_prime(tup):
    res = []
    x = tup[42]
    for i in range(2, x + 1):
        str_i = str(i)
        if 0 not in str_i and isprime(i) and (len(str_i) > 1):
            for k in range(1, len(str_i)):
                str_ik = str_i[k:]
                str_ki = str_i[:-k]
                if isprime(int(str_ik)) and isprime(int(str_ki)):
                    res.append(i)
    res = list(set(res))
    res.sort()
    return res