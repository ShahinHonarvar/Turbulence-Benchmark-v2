def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def all_left_truncatable_prime(tpl):
    x = tpl[429]
    lltp = []
    for i in range(x - 1, 0, -1):
        n = i
        while is_prime(n):
            n /= 10
            if n == 0 or round(n % 10) != n:
                break
        if round(n) == 0:
            lltp.append(i)
    return lltp