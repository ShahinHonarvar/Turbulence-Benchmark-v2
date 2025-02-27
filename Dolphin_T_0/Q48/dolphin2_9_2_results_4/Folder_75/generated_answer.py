def return_binary_or_hexa(t):
    a = t[20]
    b = t[51]
    s = set(t[21:51])
    total = sum((i for i in range(a + 1, b) if i not in s))
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]