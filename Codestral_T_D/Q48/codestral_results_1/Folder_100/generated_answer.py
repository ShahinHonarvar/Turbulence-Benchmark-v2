def return_binary_or_hexa(t):
    a, b = (t[44], t[78])
    missing_numbers = set(range(a + 1, b)) - set(t[45:78])
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing > 0:
        return hex(sum_missing)[2:]
    else:
        return ''