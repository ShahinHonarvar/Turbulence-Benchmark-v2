def return_binary_or_hexa(tup):
    a = tup[70]
    b = tup[98]
    sum_missing = sum((x for x in range(a + 1, b) if x not in tup[70:98]))
    return bin(sum_missing)[2:] if sum_missing % 2 else hex(sum_missing)[2:]