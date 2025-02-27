def return_binary_or_hexa(input_tuple):
    a = input_tuple[19]
    b = input_tuple[34]
    sum_of_numbers = sum((i for i in range(a + 1, b) if i not in input_tuple[20:35]))
    if sum_of_numbers % 2:
        return bin(sum_of_numbers)[2:]
    else:
        return hex(sum_of_numbers)[2:].upper()