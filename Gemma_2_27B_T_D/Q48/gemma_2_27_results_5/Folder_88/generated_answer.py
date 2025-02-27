def return_binary_or_hexa(input_tuple):
    a = input_tuple[3]
    b = input_tuple[9]
    sum_of_numbers = sum((x for x in range(a + 1, b) if x not in input_tuple[3:10]))
    if sum_of_numbers % 2 != 0:
        return bin(sum_of_numbers)[2:]
    else:
        return hex(sum_of_numbers)[2:].lower()