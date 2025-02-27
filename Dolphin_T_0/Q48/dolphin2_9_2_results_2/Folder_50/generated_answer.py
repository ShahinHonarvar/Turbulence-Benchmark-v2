def return_binary_or_hexa(tupl):
    a, b = (tupl[13], tupl[76])
    missing = [i for i in range(a + 1, b) if i not in tupl]
    sum_of_missing = sum(missing)
    if len(missing) == 0:
        return ''
    elif sum_of_missing % 2 == 0:
        return hex(sum_of_missing)[2:]
    else:
        return bin(sum_of_missing)[2:]