def return_binary_or_hexa(t):
    a = t[450]
    b = t[905]
    s = sum([i for i in range(a + 1, b) if i not in t[450:905]])
    if s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:]