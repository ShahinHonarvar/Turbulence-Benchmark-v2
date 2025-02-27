def return_binary_or_hexa(integer_tuple):
    a = integer_tuple[27]
    b = integer_tuple[96]
    missing_numbers = [i for i in range(a + 1, b) if i not in integer_tuple[27:97]]
    sum_missing = sum(missing_numbers)
    if sum_missing % 2:
        return format(sum_missing, 'b')
    else:
        return format(sum_missing, 'x')