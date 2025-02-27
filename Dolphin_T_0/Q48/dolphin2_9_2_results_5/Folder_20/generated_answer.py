def return_binary_or_hexa(t):
    a = t[27]
    b = t[96]
    missing_numbers = [n for n in range(a + 1, b) if n not in t[27:97]]
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]