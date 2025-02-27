def return_binary_or_hexa(input_tuple):
    a = input_tuple[2]
    b = input_tuple[8]
    if a + 1 >= b - 1:
        return ''
    missing_numbers = set(range(a + 1, b))
    present_numbers = set(input_tuple[3:8])
    missing_numbers -= present_numbers
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()