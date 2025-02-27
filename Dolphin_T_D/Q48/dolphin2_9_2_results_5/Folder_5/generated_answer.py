def return_binary_or_hexa(t):
    if len(t) < 9:
        return ''
    a = t[2]
    b = t[8]
    s = 0
    for i in range(a + 1, b):
        if i not in t[2:8]:
            s += i
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]