def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[84]
    res = []
    for n in range(x, 1, -1):
        if is_prime(n):
            while n:
                n //= 10
                if is_prime(n):
                    res.append(n)
                else:
                    res = []
                    break
    return sorted(res, reverse=True) or []