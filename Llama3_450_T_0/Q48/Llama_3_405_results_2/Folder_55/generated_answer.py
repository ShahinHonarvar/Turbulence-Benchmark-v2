def return_binary_or_hexa(t):
    a = t[10]
    b = t[12]
    s = sum((i for i in range(a + 1, b) if i not in t[11:12]))
    if s == 0:
        return ''
    elif s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]