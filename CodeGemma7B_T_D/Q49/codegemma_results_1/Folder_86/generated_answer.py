def if_decimal_is_divisible(binary):
    n = int(binary, 2)
    f = [1, 2]
    while f[-1] <= n:
        f.append(f[-2] + f[-1])
    if f.index(n) % 135 == 0:
        return True
    return False