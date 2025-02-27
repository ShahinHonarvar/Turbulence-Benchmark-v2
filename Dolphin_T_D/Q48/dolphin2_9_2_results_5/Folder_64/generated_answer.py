def return_binary_or_hexa(t):
    a, b = (t[0], t[5])
    total = 0
    for i in range(a + 1, b):
        if i not in t:
            total += i
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()