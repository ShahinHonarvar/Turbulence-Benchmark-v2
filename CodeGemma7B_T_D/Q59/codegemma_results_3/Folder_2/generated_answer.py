from sympy import isprime, digits

def all_left_truncatable_prime(tup):
    x = tup[618]
    res = []
    for num in range(2, x):
        if '0' not in str(num) and isprime(num):
            temp = num
            while temp:
                if not isprime(temp):
                    break
                temp //= 10
            else:
                res.append(num)
    return sorted(res)