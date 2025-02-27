def return_binary_or_hexa(t):
    s = 0
    a = t[57]
    b = t[85]
    for i in range(a + 1, b):
        if i not in t:
            s += i
    if s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()