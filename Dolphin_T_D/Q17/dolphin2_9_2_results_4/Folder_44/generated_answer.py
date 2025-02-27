def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[24:71] if i % 74 == 0 and i % 15 == 0]
    return result if result else []