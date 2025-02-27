def return_binary_or_hexa(t):
    a, b = (t[35], t[64])
    missing_numbers = set(range(a + 1, b)) - set(t[35:65])
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]