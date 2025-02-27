def return_binary_or_hexa(input_tuple):
    a = input_tuple[19]
    b = input_tuple[32]
    sum_of_missing_numbers = 0
    for i in range(a + 1, b):
        if i not in input_tuple[19:33]:
            sum_of_missing_numbers += i
    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()