def return_binary_or_hexa(t):
    a, b = (t[34], t[69])
    s = sum((x for x in range(a + 1, b) if x not in t[34:70]))
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]