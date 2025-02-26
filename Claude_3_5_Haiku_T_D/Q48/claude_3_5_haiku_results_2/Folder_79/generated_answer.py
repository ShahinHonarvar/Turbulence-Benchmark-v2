def return_binary_or_hexa(input_tuple):
    a = input_tuple[1]
    b = input_tuple[7]
    missing_nums = []
    for num in range(a + 1, b):
        if num not in input_tuple[1:8]:
            missing_nums.append(num)
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]