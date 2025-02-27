def return_binary_or_hexa(t):
    a = t[42]
    b = t[87]
    s = 0
    for i in range(a + 1, b):
        if i not in t:
            s += i
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]