def all_left_truncatable_prime(tup):
    x = tup[39]
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

def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True