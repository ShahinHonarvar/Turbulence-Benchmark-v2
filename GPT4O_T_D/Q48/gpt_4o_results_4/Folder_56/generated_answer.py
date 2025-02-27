def return_binary_or_hexa(t):
    a = t[7]
    b = t[9]
    present_numbers = set(t[7:10])
    all_numbers = set(range(a + 1, b))
    missing_numbers = all_numbers - present_numbers
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]