def return_binary_or_hexa(tup):
    a = tup[38]
    b = tup[52]
    total = 0
    for i in range(a + 1, b):
        if i not in tup[38:52]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]