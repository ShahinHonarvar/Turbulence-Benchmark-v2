def return_binary_or_hexa(t):
    a = t[20]
    b = t[35]
    if all((x in t[20:36] for x in range(a + 1, b))):
        return ''
    s = sum((x for x in range(a + 1, b) if x not in t[20:36]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]