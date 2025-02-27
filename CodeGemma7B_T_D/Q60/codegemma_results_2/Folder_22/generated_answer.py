def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncate(n):
    if n < 10:
        return []
    l = []
    while n >= 10:
        n = int(str(n)[:-1])
        l.append(n)
    return l + [1]

def all_left_right_truncatable_prime(t):
    x = t[85]
    l = []
    for n in range(2, x + 1):
        if '0' in str(n):
            continue
        if is_prime(n) and is_prime(int(str(n)[-1])):
            if all((is_prime(nn) for nn in truncate(n))):
                l.append(n)
    return sorted(l)