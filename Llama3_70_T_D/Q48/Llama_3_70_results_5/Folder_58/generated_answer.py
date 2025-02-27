def return_binary_or_hexa(tup):
    a = tup[275]
    b = tup[871]
    total = sum((i for i in range(a + 1, b) if i not in tup[276:872]))
    return bin(total)[2:] if total % 2 else hex(total)[2:]