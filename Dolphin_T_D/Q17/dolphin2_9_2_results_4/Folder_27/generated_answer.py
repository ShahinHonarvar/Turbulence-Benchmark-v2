def all_ints_div_by_both_two_nums(lst):
    result = [num for num in lst[20:36] if num % -36 == 0 and num % -89 == 0]
    return result if len(result) > 0 else []