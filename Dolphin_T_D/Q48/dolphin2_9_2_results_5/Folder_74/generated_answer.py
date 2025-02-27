def return_binary_or_hexa(t):
    a = t[69]
    b = t[97]
    missing_numbers = [x for x in range(a + 1, b) if x not in t]
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 != 0:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]