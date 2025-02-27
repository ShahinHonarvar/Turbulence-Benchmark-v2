def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[54:80] if i % 54 == 0 and i % 28 == 0]
    return result if result else []