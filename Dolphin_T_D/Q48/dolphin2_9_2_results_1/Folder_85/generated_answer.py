def return_binary_or_hexa(num_tuple):
    a, b = (num_tuple[1], num_tuple[8])
    missing_nums = []
    for i in range(a + 1, b):
        if i not in num_tuple:
            missing_nums.append(i)
    if not missing_nums:
        return ''
    sum_of_missing_nums = sum(missing_nums)
    if sum_of_missing_nums % 2 == 0:
        return hex(sum_of_missing_nums)[2:]
    else:
        return bin(sum_of_missing_nums)[2:]