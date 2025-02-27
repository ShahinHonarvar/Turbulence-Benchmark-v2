def all_ints_div_by_both_two_nums(lst):
    range_lst = lst[240:902]
    result = [i for i in range_lst if i % 546 == 0 and i % 709 == 0]
    return result or []