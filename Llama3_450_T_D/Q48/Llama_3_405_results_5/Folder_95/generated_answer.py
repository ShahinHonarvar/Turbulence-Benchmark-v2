def return_binary_or_hexa(t):
    a = t[32]
    b = t[99]
    present = set(t[33:99])
    total = set(range(a + 1, b))
    missing = total - present
    if not missing:
        return ''
    s = sum(missing)
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]