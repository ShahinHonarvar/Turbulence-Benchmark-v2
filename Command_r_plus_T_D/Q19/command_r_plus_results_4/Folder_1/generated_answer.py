def all_ints_not_div_by_num(lst):
    result = [num for i, num in enumerate(lst[21:69], 21) if num % -69 != 0]
    return result