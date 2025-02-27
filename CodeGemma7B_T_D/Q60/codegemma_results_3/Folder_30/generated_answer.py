def all_left_right_truncatable_prime(a):
    x = a[37]
    list_of_prime = []
    for i in range(2, x + 1):
        if is_prime(i):
            d = list(str(i))
            if '0' not in d:
                t = int(''.join(d))
                l = t
                if is_prime(t):
                    r = l
                    while r > 10:
                        r = int(str(r)[:-1])
                        if not is_prime(r):
                            break
                        l = int(str(l)[1:])
                        if not is_prime(l):
                            break
                    if r == 2 or r == 3 or r == 5 or (r == 7) or (l == 2) or (l == 3) or (l == 5) or (l == 7):
                        list_of_prime.append(t)
    return sorted(list_of_prime, reverse=True)

def is_prime(a):
    if a < 2:
        return False
    elif a == 2:
        return True
    elif a % 2 == 0:
        return False
    m = 3
    while m ** 2 <= a:
        if a % m == 0:
            return False
        m += 2
    return True