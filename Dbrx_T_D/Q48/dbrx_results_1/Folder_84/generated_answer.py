def return_binary_or_hexa(indices):
    a, b = (indices[32], indices[44])
    sum_of_missing = sum((x for x in range(a + 1, b) if x not in indices[32:45]))
    if sum_of_missing % 2 != 0:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()