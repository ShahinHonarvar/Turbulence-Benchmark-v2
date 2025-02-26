def return_binary_or_hexa(tuple_input):
    a = tuple_input[56]
    b = tuple_input[90]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in tuple_input[56:91]:
            missing_sum += num
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]