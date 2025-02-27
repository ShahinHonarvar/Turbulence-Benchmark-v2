def all_left_truncatable_prime(tup):
    l = []
    for i in range(2, tup[32]):
        if is_prime(i) and (not has_zero(i)) and left_truncatable(i):
            l.append(i)
    return sorted(l)

def left_truncatable(i):
    str1 = str(i)
    for j in range(1, len(str1)):
        if not is_prime(int(str1[j:])):
            return False
    return True

def is_prime(i):
    if i <= 1:
        return False
    for j in range(2, i):
        if i % j == 0:
            return False
    return True

def has_zero(i):
    str1 = str(i)
    if '0' in str1:
        return True
    return False