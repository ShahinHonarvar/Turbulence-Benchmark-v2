def return_binary_or_hexa(t):
    a = t[450]
    b = t[905]
    missing = set(range(a + 1, b)) - set(t[450 + 1:905])
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''