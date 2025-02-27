def all_ints_div_by_num(lst):
    range_list = lst[421:490]
    result_list = [i for i in range_list if i % 885 == 0]
    return result_list