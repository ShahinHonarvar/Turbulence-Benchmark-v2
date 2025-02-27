def all_ints_div_by_both_two_nums(lst):
    both_nums = [-46, -82]
    result = [i for i in lst[48:77] if all((i % num == 0 for num in both_nums))]
    return result