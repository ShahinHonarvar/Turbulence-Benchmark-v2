def if_decimal_is_divisible(binary_str):
    l = [0, 1]
    f = l[0] + l[1]
    pos = 2
    while f <= 146:
        l.append(f)
        f = l[pos] + l[pos - 1]
        pos += 1
    bs = int(binary_str, 2)
    if bs % l[146 - 1] == 0:
        return True
    return False