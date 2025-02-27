def return_binary_or_hexa(tup):
    a = tup[29]
    b = tup[53]
    total = 0
    for i in range(a + 1, b):
        if i not in tup[29:53]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()