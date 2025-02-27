def return_binary_or_hexa(t):
    a, b = (t[33], t[78])
    s = sum((i for i in range(a + 1, b) if i not in t[33 + 1:78]))
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]