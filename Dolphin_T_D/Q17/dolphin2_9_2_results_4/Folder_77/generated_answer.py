def all_ints_div_by_both_two_nums(lst):
    specified_range = lst[828:933]
    divisible_ints = [i for i in specified_range if i % -649 == 0 and i % -461 == 0]
    return divisible_ints