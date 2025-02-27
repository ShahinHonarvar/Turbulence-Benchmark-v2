from sympy import isprime

def truncatable_prime(n):
    if not isprime(n) or '0' in str(n):
        return False
    while n > 10:
        n = int(str(n)[1:])
        if not isprime(n):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[86]
    result = []
    for i in range(1, x + 1):
        if truncatable_prime(i):
            result.append(i)
    if result:
        result.sort(reverse=True)
    else:
        return []
    return result