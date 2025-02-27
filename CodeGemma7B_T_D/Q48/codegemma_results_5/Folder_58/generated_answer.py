def return_binary_or_hexa(tuple):
    a = tuple[275]
    b = tuple[871]
    total = 0
    for i in range(a + 1, b):
        if i not in tuple[275:872]:
            total += i
    if total & 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]