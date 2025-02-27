def is_left_right_truncatable_prime(n):
    str_n = str(n)
    length = len(str_n)
    if length < 2:
        return False
    for i in range(length):
        if str_n[i] == '0':
            return False
        if i > 0:
            left = int(str_n[:i] + str_n[i + 1:])
            if not is_prime(left):
                return False
        if i < length - 1:
            right = int(str_n[:i] + str_n[i + 1:])
            if not is_prime(right):
                return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[3]
    lst = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            lst.append(i)
    return sorted(lst, reverse=True)