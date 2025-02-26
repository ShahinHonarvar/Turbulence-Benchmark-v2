def return_binary_or_hexa(tuple_input):
    a = tuple_input[29]
    b = tuple_input[53]
    missing_nums = []
    for num in range(a + 1, b):
        if num not in tuple_input[29:54]:
            missing_nums.append(num)
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]