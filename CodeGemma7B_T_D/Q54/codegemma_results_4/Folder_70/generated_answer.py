import math
    from sympy import isprime

def all_right_truncatable_prime(t):

    def is_truncatable_prime(num):
        str_num = str(num)
        for i in range(1, len(str_num)):
            if not isprime(int(str_num[:-i])):
                return False
        return True
    res = []
    for num in t:
        if num > 433 and is_truncatable_prime(num):
            res.append(num)
    return sorted(res, reverse=True)