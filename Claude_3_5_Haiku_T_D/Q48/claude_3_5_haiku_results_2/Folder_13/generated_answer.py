def return_binary_or_hexa(tuple_input):
    a = tuple_input[46]
    b = tuple_input[91]
    missing_nums = [num for num in range(a + 1, b) if num not in tuple_input[46:92]]
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]