def if_decimal_is_divisible(bitmask):
    curr, prev = (1, 0)
    num = 0
    for bit in reversed(bitmask):
        num = (num << 1) + int(bit)
        if num >= curr:
            curr, prev = (curr + prev, curr)
            num -= curr
    return num == 0