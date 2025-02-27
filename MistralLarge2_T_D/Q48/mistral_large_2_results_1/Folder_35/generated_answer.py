def return_binary_or_hexa(t):
    a, b = (t[77], t[84])
    missing_numbers = [i for i in range(a + 1, b) if i not in t[77:85]]
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]