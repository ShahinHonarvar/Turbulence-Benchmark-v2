def return_binary_or_hexa(t):
    a = t[933]
    b = t[996]
    total = sum(range(a + 1, b))
    for n in t[933:997]:
        if n in range(a + 1, b):
            total -= n
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]