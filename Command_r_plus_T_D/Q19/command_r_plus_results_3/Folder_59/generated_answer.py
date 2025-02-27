def all_ints_not_div_by_num(lst):
    result = [num for i, num in enumerate(lst[8:9]) if num % 8 != 0]
    return result