def return_binary_or_hexa(tupl):
    a = tupl[16]
    b = tupl[87]
    missing = [i for i in range(a + 1, b) if i not in tupl[16:87]]
    sum_missing = sum(missing)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]