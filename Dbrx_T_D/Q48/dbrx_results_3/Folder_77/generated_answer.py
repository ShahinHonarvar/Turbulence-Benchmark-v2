def return_binary_or_hexa(int_tuple):
    a = int_tuple[18]
    b = int_tuple[52]
    missing_numbers = [i for i in range(a + 1, b) if i not in int_tuple[18:53]]
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return format(sum_of_missing, 'b')
    else:
        return hex(sum_of_missing)[2:].upper()