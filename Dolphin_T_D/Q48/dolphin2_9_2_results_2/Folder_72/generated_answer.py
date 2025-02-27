def return_binary_or_hexa(tuples):
    a = tuples[13]
    b = tuples[70]
    missing = [x for x in range(a + 1, b) if x not in tuples[13:71]]
    if len(missing) == 0:
        return ''
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]