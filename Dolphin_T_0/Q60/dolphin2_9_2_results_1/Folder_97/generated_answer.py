def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_right_truncatable_prime(args):
    x = args[645]
    res = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        trunc = len(str_num)
        while trunc > 1:
            if not is_prime(int(str_num[1:-1])):
                break
            trunc -= 1
        else:
            res.append(num)
    return sorted(res)