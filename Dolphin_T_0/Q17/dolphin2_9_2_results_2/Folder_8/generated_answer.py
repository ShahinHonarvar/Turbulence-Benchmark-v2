def all_ints_div_by_both_two_nums(lst):
    result = [num for num in lst[36:86] if num % -27 == 0 and num % -96 == 0]
    if not result:
        return []
    else:
        return result