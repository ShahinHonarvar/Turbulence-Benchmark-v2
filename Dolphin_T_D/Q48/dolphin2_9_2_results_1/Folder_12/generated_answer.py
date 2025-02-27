def return_binary_or_hexa(tup):
    a = tup[16]
    b = tup[87]
    missing = [i for i in range(a + 1, b) if i not in tup]
    if len(missing) == 0:
        return ''
    sum_of_missing = sum(missing)
    if sum_of_missing % 2 == 0:
        return hex(sum_of_missing)[2:]
    else:
        return bin(sum_of_missing)[2:]