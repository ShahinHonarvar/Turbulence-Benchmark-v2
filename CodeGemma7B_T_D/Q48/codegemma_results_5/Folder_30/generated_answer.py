def return_binary_or_hexa(tup):
    a, b = (tup[22], tup[24])
    L = [x for x in range(a + 1, b) if x not in tup[22:25]]
    return bin(sum(L))[2:] if sum(L) % 2 else hex(sum(L))[2:].upper()