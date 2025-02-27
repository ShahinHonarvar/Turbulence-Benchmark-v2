def return_binary_or_hexa(t):
    a = t[11]
    b = t[76]
    total = 0
    for i in range(a + 1, b):
        if i not in t[11:77]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]