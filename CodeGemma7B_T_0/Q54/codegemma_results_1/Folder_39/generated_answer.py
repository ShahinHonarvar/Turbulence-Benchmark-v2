def all_right_truncatable_prime(tup):
    x = tup[30]
    res = []
    for i in range(2, x):
        if isprime(i):
            temp = i
            while temp > 0:
                if not isprime(temp):
                    break
                temp //= 10
            else:
                res.append(i)
    res.sort(reverse=True)
    return res

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True