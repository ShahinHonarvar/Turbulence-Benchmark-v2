def return_binary_or_hexa(t):
    a = t[13]
    b = t[76]
    missing = [i for i in range(a + 1, b) if i not in t[13:77]]
    s = sum(missing)
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]