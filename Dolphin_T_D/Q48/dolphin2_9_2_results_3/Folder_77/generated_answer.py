def return_binary_or_hexa(t):
    a, b = (t[18], t[52])
    s = sum((x for x in range(a + 1, b) if x not in t[19:51]))
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]