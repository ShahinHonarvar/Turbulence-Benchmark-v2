def return_binary_or_hexa(t):
    a = t[933]
    b = t[996]
    total = 0
    for i in range(a + 1, b):
        if not i in t:
            total += i
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]