def return_binary_or_hexa(t):
    a, b = (t[2], t[5])
    s = sum((i for i in range(a + 1, b) if i not in t[2:6]))
    if not s:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()