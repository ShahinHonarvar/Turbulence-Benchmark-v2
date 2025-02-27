def return_binary_or_hexa(tuple_arg):
    a = tuple_arg[44]
    b = tuple_arg[78]
    missing_numbers = set(range(a + 1, b)) - set(tuple_arg[45:78])
    if not missing_numbers:
        return ''
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:].upper()