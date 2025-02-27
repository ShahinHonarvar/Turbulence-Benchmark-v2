def all_left_truncatable_prime(t):
    return sorted([i for i in t if is_prime(i) and int(str(i)[1:]) is not 0 and all((is_prime(int(str(i)[:j])) for j in range(1, len(str(i)))))], reverse=True)

def is_prime(x):
    if x <= 1:
        return False
    if x in (2, 3):
        return True
    if x % 6 not in (1, 5):
        return False
    m, s = (int(x ** 0.5) + 1, 6)
    while s <= m:
        if x % s == 0 or x % (s + 2) == 0:
            return False
        s += 6
    return True