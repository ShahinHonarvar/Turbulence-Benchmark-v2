def all_left_truncatable_prime(t):
    x = t[35]
    res = []
    for i in range(2, x):
        if isprime(i) and (not has_zero(i)):
            temp = i
            while temp > 0:
                if not isprime(temp):
                    break
                temp //= 10
            else:
                res.append(i)
    res.sort(reverse=True)
    return res

def isprime(i):
    if i <= 1:
        return False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True

def has_zero(i):
    return '0' in str(i)