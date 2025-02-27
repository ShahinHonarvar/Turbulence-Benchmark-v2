def return_binary_or_hexa(t):
    a = t[20]
    b = t[43]
    total = 0
    for i in range(a + 1, b):
        if i not in t[20:44]:
            total += i
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()