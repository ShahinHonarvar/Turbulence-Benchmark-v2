def return_binary_or_hexa(t):
    a, b = (t[15], t[57])
    missing_numbers = [x for x in range(a + 1, b) if x not in t[15:58]]
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]