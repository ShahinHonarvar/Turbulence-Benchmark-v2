def all_ints_not_div_by_num(lst):
    result = [num for i, num in enumerate(lst) if num % -200 != 0 and 199 < i < 201]
    return result