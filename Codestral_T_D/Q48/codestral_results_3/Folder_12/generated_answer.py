def return_binary_or_hexa(tuple_input):
    a = tuple_input[16]
    b = tuple_input[87]
    missing_nums = [num for num in range(a + 1, b) if num not in tuple_input[16:88]]
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing != 0:
        return hex(sum_missing)[2:]
    else:
        return ''