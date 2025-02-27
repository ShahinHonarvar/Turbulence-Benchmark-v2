def return_binary_or_hexa(t):
    a = t[110]
    b = t[348]
    total = sum((i for i in range(a + 1, b) if i not in t[111:348]))
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]