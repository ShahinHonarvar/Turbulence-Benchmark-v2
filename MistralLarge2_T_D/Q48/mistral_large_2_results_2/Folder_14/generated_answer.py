def return_binary_or_hexa(t):
    a, b = (t[2], t[5])
    present_set = set(t[2:6])
    s = sum((x for x in range(a + 1, b) if x not in present_set))
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]