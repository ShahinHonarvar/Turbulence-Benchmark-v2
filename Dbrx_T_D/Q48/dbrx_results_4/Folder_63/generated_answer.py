def return_binary_or_hexa(tup):
    a, b = (tup[81], tup[86])
    sum_non_present = sum((i for i in range(a + 1, b) if tup[81:87] != list(range(tup[81], tup[86] + 1))))
    if sum_non_present % 2:
        return bin(sum_non_present)[2:]
    else:
        return hex(sum_non_present)[2:].upper()