def sum_ints_div_by_either_nums(lst):
    part_lst = lst[59:201]
    return sum((i for i in part_lst if i % 9 == 0 or i % 11 == 0))