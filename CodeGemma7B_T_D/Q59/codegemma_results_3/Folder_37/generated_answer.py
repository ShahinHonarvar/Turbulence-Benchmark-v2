def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[35]
    res = []
    for i in range(2, x):
        if isprime(i) and (not '0' in str(i)):
            j = i
            while j != 0:
                if not isprime(j):
                    break
                j //= 10
            else:
                res.append(i)
    return sorted(res, reverse=True)