def all_ints_not_div_by_num(lst):
    result = [num for i, num in enumerate(lst[91:98]) if num % 13 != 0]
    return result