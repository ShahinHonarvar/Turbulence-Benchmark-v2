def return_binary_or_hexa(t):
    a = t[11]
    b = t[76]
    s = 0
    for i in range(a + 1, b):
        if i not in t[12:76]:
            s += i
    if s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]