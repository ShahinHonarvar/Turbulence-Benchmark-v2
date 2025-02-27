def return_binary_or_hexa(t):
    a, b = (t[3], t[8])
    s = 0
    for i in range(a + 1, b):
        if i not in t[3:9]:
            s += i
    if s % 2:
        return str(s)
    else:
        return hex(s)[2:].upper()