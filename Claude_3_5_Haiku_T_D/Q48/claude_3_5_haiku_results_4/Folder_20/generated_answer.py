def return_binary_or_hexa(input_tuple):
    a = input_tuple[27]
    b = input_tuple[96]
    missing_nums_sum = 0
    for num in range(a + 1, b):
        if num not in input_tuple[27:97]:
            missing_nums_sum += num
    if missing_nums_sum == 0:
        return ''
    if missing_nums_sum % 2 == 1:
        return bin(missing_nums_sum)[2:]
    else:
        return hex(missing_nums_sum)[2:]