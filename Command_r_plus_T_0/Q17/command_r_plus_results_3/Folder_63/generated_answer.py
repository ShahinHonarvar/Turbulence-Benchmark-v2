def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[31:51] if i % 81 == 0 and i % 64 == 0]
    return result