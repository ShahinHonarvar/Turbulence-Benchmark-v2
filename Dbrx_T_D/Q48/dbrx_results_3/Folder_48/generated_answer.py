def return_binary_or_hexa(sorted_tuple):
    a = sorted_tuple[933]
    b = sorted_tuple[996]
    missing_numbers = [i for i in range(a + 1, b) if i not in sorted_tuple[933:997]]
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()