def return_binary_or_hexa(tup):
    a, b = (tup[36], tup[85])
    total = sum(range(a + 1, b)) - sum(tup[36:86])
    return bin(total)[-1] if total % 2 else hex(total)[2:].upper()