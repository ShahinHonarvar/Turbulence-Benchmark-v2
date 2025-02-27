def return_binary_or_hexa(t):
    a, b = (t[90], t[200])
    s = 0
    for i in range(a + 1, b):
        if i not in t:
            s += i
    if s != 0:
        if s % 2 == 0:
            return hex(s)[2:]
        else:
            return bin(s)[2:]
    else:
        return ''