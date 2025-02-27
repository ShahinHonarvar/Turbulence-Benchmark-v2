def all_ints_div_by_both_two_nums(lst):
    return [lst[i] for i in range(86, 90) if lst[i] % -61 == 0 and lst[i] % -79 == 0 and (i < len(lst))]