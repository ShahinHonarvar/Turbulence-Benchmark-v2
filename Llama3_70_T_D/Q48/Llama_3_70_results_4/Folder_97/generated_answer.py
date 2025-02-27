def return_binary_or_hexa(t):
    a = t[34]
    b = t[69]
    s = sum((i for i in range(a + 1, b) if i not in t[34:70]))
    if s == 0:
        return ''
    if s % 2:
        return bin(s)[2:]
    return hex(s)[2:]