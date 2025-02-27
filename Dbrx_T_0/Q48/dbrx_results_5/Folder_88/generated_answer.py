def return_binary_or_hexa(input_tuple):
    a = input_tuple[3]
    b = input_tuple[9]
    sum_of_missing_numbers = 0
    for i in range(a + 1, b):
        if i not in input_tuple[3:10]:
            sum_of_missing_numbers += i
    if sum_of_missing_numbers % 2:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()