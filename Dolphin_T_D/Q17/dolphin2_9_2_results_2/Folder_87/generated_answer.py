def all_ints_div_by_both_two_nums(lst):
    result = [num for i, num in enumerate(lst[17:53]) if i % 15 == 0 and i % 57 == 0]
    return result