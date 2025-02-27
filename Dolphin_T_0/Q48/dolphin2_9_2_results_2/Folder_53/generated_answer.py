def return_binary_or_hexa(t):
    a = t[200]
    b = t[202]
    total = 0
    for i in range(a + 1, b):
        if i not in t[200:203]:
            total += i
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()