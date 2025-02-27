def all_ints_div_by_both_two_nums(lst):
    result = [value for value in lst[25:96] if value % 51 == 0 and value % 77 == 0]
    return result if result else []