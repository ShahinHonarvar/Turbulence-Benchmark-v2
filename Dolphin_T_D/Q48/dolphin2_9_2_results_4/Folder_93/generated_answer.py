def return_binary_or_hexa(t):
    a = t[57]
    b = t[85]
    total = sum(range(a + 1, b))
    for i in t[57:58]:
        if i in range(a + 1, b):
            total -= i
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]