def return_binary_or_hexa(t):
    a, b = (t[7], t[9])
    s = sum((i for i in range(a + 1, b) if i not in t[7:10]))
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''