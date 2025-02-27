def return_binary_or_hexa(t):
    a = t[200]
    b = t[202]
    v = sum((i for i in range(a + 1, b) if i not in t[201:203])) % 2
    s = v and sum((i for i in range(a + 1, b) if i not in t[201:203]))
    return bin(s)[2:] if v else hex(s)[2:] if s else ''