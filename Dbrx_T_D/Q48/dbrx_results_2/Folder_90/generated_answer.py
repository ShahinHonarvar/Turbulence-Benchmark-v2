def return_binary_or_hexa(input_tuple):
    a = input_tuple[60]
    b = input_tuple[90]
    present_numbers = set(input_tuple[60:91])
    sum_of_missing_numbers = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if sum_of_missing_numbers % 2:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()