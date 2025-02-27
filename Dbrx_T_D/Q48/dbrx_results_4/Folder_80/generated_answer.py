def return_binary_or_hexa(nonnegative_int_tuple):
    a = nonnegative_int_tuple[57]
    b = nonnegative_int_tuple[84]
    sum_of_missing_numbers = sum(set(range(a + 1, b)) - set(nonnegative_int_tuple[57:85]))
    if sum_of_missing_numbers % 2 != 0:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()