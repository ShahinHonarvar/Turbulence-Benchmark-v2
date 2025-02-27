def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(t):
    x = t[429]
    ret = []
    for n in range(2, x + 1):
        if n % 10 == 0:
            continue
        if n % 5 == 0 or n % 2 == 0:
            continue
        sn = set(map(int, str(n)))
        if len(sn) != len(str(n)) or (n < 10 and n not in sn):
            continue
        if is_prime(n):
            trunc = n
            while trunc > 9:
                if not is_prime(trunc):
                    break
                trunc = int(str(trunc)[1:-1])
            else:
                ret.append(n)
    return sorted(ret, reverse=True)