def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[0]
    res = []
    for i in range(2, x + 1):
        str_i = str(i)
        if '0' in str_i:
            continue
        while len(str_i) > 1:
            if not is_prime(int(str_i)):
                break
            str_i = str_i[1:-1]
        else:
            res.append(i)
    return res