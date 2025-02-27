def return_binary_or_hexa(tup):
    a = tup[46]
    b = tup[91]
    total = 0
    for i in range(a + 1, b):
        if i not in tup[46:92]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]