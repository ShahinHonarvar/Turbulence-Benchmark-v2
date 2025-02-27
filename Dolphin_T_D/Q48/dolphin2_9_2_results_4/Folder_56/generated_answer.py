def return_binary_or_hexa(t):
    a = t[7]
    b = t[9]
    s = sum(set([i for i in range(a + 1, b) if i not in t[7:9 + 1]]) & set(range(a + 1, b)))
    if s % 2 != 0:
        return bin(s).replace('0b', '')
    else:
        return hex(s).replace('0x', '')