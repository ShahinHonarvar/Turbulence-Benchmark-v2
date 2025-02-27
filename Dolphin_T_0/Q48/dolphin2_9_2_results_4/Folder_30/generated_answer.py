def return_binary_or_hexa(t):
    a = t[22]
    b = t[24]
    can_sum = set(range(a + 1, b))
    can_sum -= set(t[23])
    s = sum(can_sum)
    if s % 2:
        return bin(s).replace('0b', '')
    else:
        return hex(s).replace('0x', '')