def return_binary_or_hexa(tuple_input):
    a = tuple_input[10]
    b = tuple_input[12]
    missing_nums = []
    for num in range(a + 1, b):
        if num not in tuple_input[10:13]:
            missing_nums.append(num)
    total_sum = sum(missing_nums)
    if not missing_nums:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]