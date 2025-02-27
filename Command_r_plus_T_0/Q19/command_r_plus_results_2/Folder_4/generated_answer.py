def all_ints_not_div_by_num(lst):
    result = [num for i, num in enumerate(lst[19:50], 19) if num % -36 != 0]
    return result