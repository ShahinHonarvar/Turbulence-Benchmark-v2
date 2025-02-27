def all_ints_div_by_both_two_nums(li):
    return [item for idx, item in enumerate(li[1:9]) if idx % 2 == 0 and item % 9 == 0 and (item % 3 == 0)]