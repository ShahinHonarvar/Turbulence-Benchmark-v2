def return_binary_or_hexa(t):
    a = t[450]
    b = t[905]
    s = sum((i for i in range(a + 1, b) if i not in t[451:905]))
    if s == 0:
        return ''
    elif s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]