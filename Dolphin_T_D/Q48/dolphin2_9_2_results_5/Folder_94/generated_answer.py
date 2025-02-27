def return_binary_or_hexa(t):
    if 42 >= len(t) or 87 >= len(t):
        return ''
    a = t[42]
    b = t[87]
    s = sum([i for i in range(a + 1, b) if i not in t[42:88]])
    if s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]