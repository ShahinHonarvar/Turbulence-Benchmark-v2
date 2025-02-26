def return_binary_or_hexa(input_tuple):
    a = input_tuple[20]
    b = input_tuple[51]
    missing_numbers_sum = 0
    for num in range(a + 1, b):
        if num not in input_tuple[20:52]:
            missing_numbers_sum += num
    if missing_numbers_sum == 0:
        return ''
    if missing_numbers_sum % 2 == 1:
        return bin(missing_numbers_sum)[2:]
    else:
        return hex(missing_numbers_sum)[2:]