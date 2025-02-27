def all_left_truncatable_prime(tu):
    x = tu[25]
    res = []
    for i in range(2, x):
        if isprime(i) and '0' not in str(i):
            temp = i
            while temp > 0:
                if not isprime(temp):
                    break
                temp = int(str(temp)[1:])
            else:
                res.append(i)
    return sorted(res, reverse=True)