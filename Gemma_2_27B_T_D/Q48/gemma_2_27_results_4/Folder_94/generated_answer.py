def return_binary_or_hexa(t):
    a = t[42]
    b = t[87]
    total = sum([i for i in range(a + 1, b) if i not in t[42:87]])
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]