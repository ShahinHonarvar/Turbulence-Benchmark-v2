def return_binary_or_hexa(input_tuple):
    a = input_tuple[86]
    b = input_tuple[90]
    sum_of_missing_numbers = 0
    for num in range(a + 1, b):
        if num not in input_tuple[86:91]:
            sum_of_missing_numbers += num
    if sum_of_missing_numbers % 2:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers).split('x')[-1].upper()