def all_right_truncatable_prime(t):
    x = t[70]
    res = []
    for a in range(2, x - 1):
        if all_prime(a):
            if is_truncatable_prime(a):
                res.append(a)
    if res == []:
        return []
    return sorted(res, reverse=True)

def is_truncatable_prime(a):
    str_a = str(a)
    list_a = list(str_a)
    for b in range(1, len(list_a)):
        list_a.pop()
        str_a = ''.join(list_a)
        if not all_prime(int(str_a)):
            return False
    return True

def all_prime(a):
    if a <= 1:
        return False
    for b in range(2, a):
        if a % b == 0:
            return False
    return True