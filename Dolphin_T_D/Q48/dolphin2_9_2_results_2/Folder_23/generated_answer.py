def return_binary_or_hexa(tuple_input):
    a = tuple_input[20]
    b = tuple_input[36]
    missing_nums = [num for num in range(a + 1, b) if num not in tuple_input[20:37]]
    if not missing_nums:
        return ''
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 0:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:]