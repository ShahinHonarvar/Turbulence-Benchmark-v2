def return_binary_or_hexa(input_tuple):
    a = input_tuple[2]
    b = input_tuple[8]
    sum_of_missing_numbers = sum(range(a + 1, b)) - sum(input_tuple[3:8])
    if sum_of_missing_numbers % 2:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers).split('x')[-1].upper()