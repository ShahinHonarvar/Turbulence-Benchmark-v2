def return_binary_or_hexa(tuple_nums):
    a = tuple_nums[17]
    b = tuple_nums[88]
    missing_nums_sum = 0
    for num in range(a + 1, b):
        if num not in tuple_nums[17:89]:
            missing_nums_sum += num
    if missing_nums_sum == 0:
        return ''
    if missing_nums_sum % 2 == 1:
        return bin(missing_nums_sum)[2:]
    else:
        return hex(missing_nums_sum)[2:]