def all_left_truncatable_prime(t):
    x = t[97]
    r = []
    for a in range(2, x):
        if is_prime(a) and (not has_zero(a)) and is_all_prime(to_lefttruncatable_list(a)):
            r.append(a)
    return sorted(r, reverse=True)

def has_zero(n):
    while n != 0:
        if n % 10 == 0:
            return True
        n //= 10
    return False

def is_prime(n):
    if n < 2:
        return False
    elif n in [2, 3, 5]:
        return True
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def to_lefttruncatable_list(n):
    r = []
    while n != 0:
        r.append(n)
        n //= 10
    r.reverse()
    return r

def is_all_prime(l):
    for n in l:
        if not is_prime(n):
            return False
    return True