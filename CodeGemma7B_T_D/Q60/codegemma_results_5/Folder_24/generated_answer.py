from sympy import isprime

def all_left_right_truncatable_prime(x):
    str_x = str(x)
    res = []
    for n in range(2, int(str_x) + 1):
        if len(str(n)) <= 2 and isprime(n):
            continue
        if '0' not in str(n) and isprime(n):
            temp = str(n)
            l, r = (temp[0], temp[-1])
            while len(temp) > 2 and isprime(int(temp)):
                l, r = (temp[0], temp[-1])
                temp = temp[1:-1]
            if len(temp) <= 2 and isprime(int(temp)):
                res.append(int(str_x))
    return sorted(res, reverse=True) if res else []