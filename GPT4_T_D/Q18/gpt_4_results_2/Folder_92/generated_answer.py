def sum_ints_div_by_either_nums(int_list):
    if not int_list:
        return 0
    start_index, end_index = (0, 0)
    range_list = int_list[start_index:end_index + 1]
    sum_nums = sum(filter(lambda x: isinstance(x, int), range_list))
    return sum_nums