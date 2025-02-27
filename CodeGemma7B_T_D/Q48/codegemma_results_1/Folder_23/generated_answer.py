def return_binary_or_hexa(tup):
    a, b = (tup[20], tup[36])
    total = 0
    for i in range(a + 1, b):
        if i not in tup[20:37]:
            total += i
    if total % 2:
        return bin(total)[2:]
    return hex(total)[2:].upper()