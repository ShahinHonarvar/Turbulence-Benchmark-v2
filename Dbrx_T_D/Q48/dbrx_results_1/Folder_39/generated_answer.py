def return_binary_or_hexa(input_tuple):
    a = input_tuple[44]
    b = input_tuple[91]
    if a + 1 >= b - 1:
        return ''
    missing_numbers = set(range(a + 1, b))
    for num in input_tuple[44:92]:
        if num in missing_numbers:
            missing_numbers.remove(num)
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()