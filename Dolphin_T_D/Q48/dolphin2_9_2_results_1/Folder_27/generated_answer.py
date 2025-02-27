def return_binary_or_hexa(t):
    a = t[86]
    b = t[89]
    s = sum(set([i for i in range(a + 1, b)]) - set(t[87:89]))
    if s % 2:
        return bin(s).replace('0b', '')
    else:
        return hex(s).replace('0x', '')