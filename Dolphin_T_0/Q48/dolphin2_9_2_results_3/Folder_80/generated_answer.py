def return_binary_or_hexa(t):
    a = t[57]
    b = t[84]
    if a + 1 == b or a == b:
        return ''
    s = sum(set(range(a + 1, b)) - set(t[57:85]))
    if s % 2 == 1:
        return bin(s)[2:]
    return hex(s)[2:]