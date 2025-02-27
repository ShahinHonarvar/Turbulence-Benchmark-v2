def return_binary_or_hexa(integer_tuple):
    a = integer_tuple[3]
    b = integer_tuple[9]
    missing_numbers = set(range(a + 1, b)) - set(integer_tuple[4:9])
    if not missing_numbers:
        return ''
    else:
        sum_of_missing = sum(missing_numbers)
        if sum_of_missing % 2:
            return bin(sum_of_missing)[2:]
        else:
            return hex(sum_of_missing)[2:].upper()