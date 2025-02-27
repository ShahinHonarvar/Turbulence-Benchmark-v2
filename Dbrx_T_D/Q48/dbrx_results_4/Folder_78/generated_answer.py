def return_binary_or_hexa(tup):
    a, b = (tup[62], tup[96])
    sum_not_present = sum((i for i in range(a + 1, b) if i not in tup[62:97]))
    if sum_not_present % 2:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:].upper()