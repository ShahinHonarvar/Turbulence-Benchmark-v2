def return_binary_or_hexa(input_tuple):
    a = input_tuple[86]
    b = input_tuple[99]
    total_range = list(range(a + 1, b))
    sublist = input_tuple[86:100]
    not_in_sublist = [i for i in total_range if i not in sublist]
    sum_numbers_not_in_sublist = sum(not_in_sublist)
    if sum_numbers_not_in_sublist % 2 != 0:
        return bin(sum_numbers_not_in_sublist)[2:]
    else:
        return hex(sum_numbers_not_in_sublist)[2:]