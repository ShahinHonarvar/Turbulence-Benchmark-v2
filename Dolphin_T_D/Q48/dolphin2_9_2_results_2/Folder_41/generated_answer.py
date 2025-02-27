def return_binary_or_hexa(tup):
    a = tup[3]
    b = tup[8]
    missing = [i for i in range(a + 1, b) if i not in tup]
    sum_missing = sum(missing)
    if sum_missing % 2 != 0:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()