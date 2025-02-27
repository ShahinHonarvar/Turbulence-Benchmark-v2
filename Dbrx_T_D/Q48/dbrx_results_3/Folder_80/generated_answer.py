def return_binary_or_hexa(integer_tuple):
    a = integer_tuple[57]
    b = integer_tuple[84]
    non_present_numbers = set(range(a + 1, b)) - set(integer_tuple[58:84])
    if not non_present_numbers:
        return ''
    sum_of_numbers = sum(non_present_numbers)
    if sum_of_numbers % 2:
        return bin(sum_of_numbers)[2:]
    else:
        return hex(sum_of_numbers)[2:].upper()