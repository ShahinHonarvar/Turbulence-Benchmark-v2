def all_ints_div_by_both_two_nums(lst):
    range_lst = lst[299:383]
    result = [i for i in range_lst if i % 858 == 0 and i % 952 == 0]
    return result if result else []