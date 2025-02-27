def return_binary_or_hexa(t):
    a = t[60]
    b = t[200]
    s = sum((i for i in range(a + 1, b) if i not in t[60:201]))
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''