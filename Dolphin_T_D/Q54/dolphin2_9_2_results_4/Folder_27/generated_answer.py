from sympy import isprime

def all_right_truncatable_prime(a):
    x = a[79]
    res = []
    for i in range(2, x):
        if isprime(i):
            flag = True
            for j in str(i):
                if not isprime(int(i // 10 ** j)):
                    flag = False
                    break
            if flag:
                res.append(i)
    return sorted(res, reverse=True) if res else []