def all_left_right_truncatable_prime(t):
    x = t[54]
    y = []
    for i in range(2, x + 1):
        if '0' not in str(i) and is_prime(i) and is_truncatable_prime(i):
            y.append(i)
    return sorted(y, reverse=True)

def is_prime(i):
    if i <= 1:
        return False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True

def is_truncatable_prime(i):
    l = len(str(i))
    for j in range(1, l // 2 + 1):
        if not is_prime(int(str(i)[:j])):
            return False
        if not is_prime(int(str(i)[j:])):
            return False
    return True