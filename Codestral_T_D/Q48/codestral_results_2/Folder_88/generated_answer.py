def return_binary_or_hexa(tupl):
    a, b = (tupl[3], tupl[9])
    missing = set(range(a + 1, b)) - set(tupl[3:9])
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing > 0:
        return hex(sum_missing)[2:]
    else:
        return ''