def return_binary_or_hexa(input_tuple):
    a = input_tuple[17]
    b = input_tuple[88]
    missing_nums = [num for num in range(a + 1, b) if num not in input_tuple[17:89]]
    if len(missing_nums) == 0:
        return ''
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:]