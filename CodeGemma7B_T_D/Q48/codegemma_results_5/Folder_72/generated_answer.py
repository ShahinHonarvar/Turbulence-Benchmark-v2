def return_binary_or_hexa(t):
    a = t[13]
    b = t[70]
    s = 0
    for i in range(a + 1, b):
        if i not in t[13:71]:
            s += i
    if s & 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()