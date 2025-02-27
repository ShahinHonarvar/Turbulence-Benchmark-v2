def all_ints_div_by_both_two_nums(lst):
    ans = [i for i in lst[0:6] if i % 13 == 0 and i % -1 == 0]
    return ans or []