def return_binary_or_hexa(input_tuple):
    a = input_tuple[15]
    b = input_tuple[57]
    sum_of_numbers = sum(set(range(a + 1, b)) - set(input_tuple[15:57]))
    if sum_of_numbers % 2:
        return bin(sum_of_numbers)[2:]
    else:
        return hex(sum_of_numbers)[2:].upper()