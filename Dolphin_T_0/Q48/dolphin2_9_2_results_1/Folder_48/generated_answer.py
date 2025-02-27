def return_binary_or_hexa(t):
    a = t[933]
    b = t[996]
    s = sum((i for i in range(a + 1, b) if i not in t))
    if s % 2 == 0:
        return str(hex(s))[2:].upper()
    else:
        return str(bin(s))[2:]