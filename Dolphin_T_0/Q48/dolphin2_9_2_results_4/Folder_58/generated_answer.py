def return_binary_or_hexa(lst):
    a = lst[275]
    b = lst[871]
    total = sum(range(a + 1, b)) - sum(lst[276:871])
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()