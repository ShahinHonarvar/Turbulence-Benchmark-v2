def all_ints_div_by_both_two_nums(lst):
    result = [x for x in lst[240:902] if x % 546 == 0 and x % 709 == 0]
    return result if result else []