def return_binary_or_hexa(tuple_input):
    a = tuple_input[39]
    b = tuple_input[43]
    segment = set(tuple_input[39:44])
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in segment:
            missing_sum += num
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]