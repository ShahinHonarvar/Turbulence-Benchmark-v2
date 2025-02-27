def all_ints_div_by_both_two_nums(lst):
    return [lst[i] for i in range(10, 29) if lst[i] % -61 == 0 and lst[i] % -64 == 0]