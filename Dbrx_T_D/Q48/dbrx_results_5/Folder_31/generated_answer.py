def return_binary_or_hexa(input_tuple):
    a = input_tuple[33]
    b = input_tuple[78]
    non_present_numbers = []
    for num in range(a + 1, b):
        if num not in input_tuple[a:b]:
            non_present_numbers.append(num)
    if not non_present_numbers:
        return ''
    sum_of_non_present_numbers = sum(non_present_numbers)
    if sum_of_non_present_numbers % 2:
        binary_representation = bin(sum_of_non_present_numbers)[2:]
        return binary_representation
    else:
        hexadecimal_representation = hex(sum_of_non_present_numbers)[2:].upper()
        return hexadecimal_representation