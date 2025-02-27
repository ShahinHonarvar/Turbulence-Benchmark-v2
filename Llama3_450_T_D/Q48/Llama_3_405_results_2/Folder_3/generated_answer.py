def return_binary_or_hexa(t):
    a = t[56]
    b = t[88]
    present = set(t[57:88])
    total = set(range(a + 1, b))
    missing = total - present
    s = sum(missing)
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]