def return_binary_or_hexa(input_tuple):
    a = input_tuple[10]
    b = input_tuple[76]
    all_numbers_in_range = set(range(a + 1, b + 1))
    numbers_in_tuple = set(input_tuple[11:76])
    missing_numbers = all_numbers_in_range - numbers_in_tuple
    if not missing_numbers:
        return ''
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2 != 0:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:]