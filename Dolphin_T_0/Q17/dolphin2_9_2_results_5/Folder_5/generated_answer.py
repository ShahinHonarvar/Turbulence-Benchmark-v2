def all_ints_div_by_both_two_nums(lst):
    result = [[i] for i in lst[0:2] if i % -6 == 0 and i % 4 == 0]
    return [item for sublist in result for item in sublist]