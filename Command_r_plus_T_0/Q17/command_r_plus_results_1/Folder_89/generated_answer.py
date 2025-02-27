def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[28:97] if i % 90 == 0 and i % 97 == 0]
    return result