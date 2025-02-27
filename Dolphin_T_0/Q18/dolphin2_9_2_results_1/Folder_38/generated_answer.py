def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst[9:77]) if i % 40 == 0 or i % 12 == 0))