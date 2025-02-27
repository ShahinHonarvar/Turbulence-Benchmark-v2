def return_binary_or_hexa(t):
    a, b = (t[27], t[96])
    s = sum((i for i in range(a + 1, b) if i not in t[27:96]))
    if s == 0:
        return ''
    elif s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]