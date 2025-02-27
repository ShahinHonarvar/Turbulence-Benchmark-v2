def all_ints_not_div_by_num(lst):
    result = [num for i, num in enumerate(lst[266:586], 266) if num % 840 != 0]
    return result