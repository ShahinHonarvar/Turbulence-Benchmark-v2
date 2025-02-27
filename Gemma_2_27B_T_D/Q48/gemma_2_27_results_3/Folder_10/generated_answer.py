def return_binary_or_hexa(t):
    a = t[36]
    b = t[54]
    total = 0
    for i in range(a + 1, b):
        if i not in t[36:55]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]