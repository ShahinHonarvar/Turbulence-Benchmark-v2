def return_binary_or_hexa(tuple_input):
    a = tuple_input[18]
    b = tuple_input[52]
    all_nums_in_range = set(range(a + 1, b))
    local_set = set(tuple_input[18:53])
    not_in_tuple = all_nums_in_range - local_set
    sum_nums = sum(not_in_tuple)
    if sum_nums % 2 == 0:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:]