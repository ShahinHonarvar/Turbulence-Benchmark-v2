def all_left_truncatable_prime(a):
    o = []
    x = a[46]
    for i in range(2, x):
        if is_prime(i) and str(i).find('0') == -1:
            j = 2
            s = int(str(i)[-j:])
            while j <= len(str(i)) and is_prime(s):
                j += 1
                s = int(str(i)[-j:])
            if j >= len(str(i)):
                o.append(i)
    return sorted(o, reverse=True)

def is_prime(p):
    if p <= 1:
        return False
    elif p <= 3:
        return True
    elif p % 2 == 0 or p % 3 == 0:
        return False
    for i in range(5, int(p ** 0.5) + 1, 6):
        if p % i == 0 or p % (i + 2) == 0:
            return False
    return True