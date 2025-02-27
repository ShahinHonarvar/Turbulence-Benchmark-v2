def return_binary_or_hexa(t):
    a = t[1]
    b = t[7]
    s = sum((i for i in range(a + 1, b) if i not in t[1:8]))
    if s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:]