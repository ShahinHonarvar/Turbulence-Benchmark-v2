def return_binary_or_hexa(t):
    a, b = (t[0], t[6])
    s = sum((i for i in range(a + 1, b) if i not in t[1:6]))
    if s:
        if s % 2:
            return bin(s)[2:]
        else:
            return hex(s)[2:]
    else:
        return ''