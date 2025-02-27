def all_right_truncatable_prime(arg):
    x = arg[97]
    p = 2
    result = []
    while p < x:
        m = 0
        while p + m <= x and (p + m) % 2 == 0:
            if p + m == x:
                break
            m += 2
        if m == 0 or (p + m) * (p + m) > x:
            p += 2
            continue
        kk = p
        flag = True
        while kk > 0:
            if kk % 10 == 0 or not is_prime(kk):
                flag = False
                break
            kk //= 10
        if flag:
            result.append(p)
        p += 2
    return sorted(result)

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True