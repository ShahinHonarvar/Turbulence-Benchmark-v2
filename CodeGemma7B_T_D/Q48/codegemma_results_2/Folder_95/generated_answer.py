def return_binary_or_hexa(t):
    a, b = (t[32], t[99])
    s = 0
    for i in range(a + 1, b):
        if i not in t[32:100]:
            s += i
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()