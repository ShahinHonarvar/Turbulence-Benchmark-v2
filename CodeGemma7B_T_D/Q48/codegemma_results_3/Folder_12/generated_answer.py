def return_binary_or_hexa(tup):
    a = tup[16]
    b = tup[87]
    broken_set = set((x for x in range(a + 1, b))) - set(tup[16:88])
    if sum(broken_set) % 2:
        return bin(sum(broken_set))[2:]
    return hex(sum(broken_set))[2:].upper()