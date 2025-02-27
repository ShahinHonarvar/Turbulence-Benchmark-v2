def all_ints_div_by_num(num_list):
    if not isinstance(num_list, list):
        return []
    range_nums = num_list[59:98]
    div_by_neg_thirty_six = [num for num in range_nums if num % -36 == 0]
    return div_by_neg_thirty_six