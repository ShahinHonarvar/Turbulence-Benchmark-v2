def return_binary_or_hexa(input_tuple):
    a = input_tuple[81]
    b = input_tuple[86]
    sum_of_missing_numbers = sum(range(a + 1, b)) - sum(input_tuple[82:86])
    if sum_of_missing_numbers % 2 == 0:
        return hex(sum_of_missing_numbers)
    else:
        return bin(sum_of_missing_numbers)[2:]