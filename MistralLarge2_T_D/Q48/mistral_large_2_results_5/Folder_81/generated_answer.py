def return_binary_or_hexa(t):
    a, b = (t[10], t[100])
    s = sum((x for x in range(a + 1, b) if x not in t[10:101]))
    if not s:
        return ''
    return bin(s)[2:] if s % 2 else hex(s)[2:]