def all_ints_div_by_both_two_nums(lst):
    divisible_by_72_and_70 = [i for i in lst[69:71] if i % 72 == 0 and i % 70 == 0]
    return divisible_by_72_and_70