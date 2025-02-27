def return_binary_or_hexa(input_tuple):
    a = input_tuple[7]
    b = input_tuple[9]
    missing_numbers = [i for i in range(a + 1, b) if i not in input_tuple[7:9]]
    if not missing_numbers:
        return ''
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()