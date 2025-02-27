def return_binary_or_hexa(t):
    a = t[10]
    b = t[100]
    present = set(t[11:100])
    total = set(range(a + 1, b))
    missing = total - present
    s = sum(missing)
    if s == 0:
        return ''
    elif s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]