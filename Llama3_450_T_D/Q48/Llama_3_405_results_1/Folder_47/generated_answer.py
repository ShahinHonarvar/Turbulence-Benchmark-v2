def return_binary_or_hexa(t):
    a = t[29]
    b = t[53]
    present = set(t[30:53])
    total = set(range(a + 1, b))
    absent = total - present
    s = sum(absent)
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]