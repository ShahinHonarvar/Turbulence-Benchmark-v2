def all_ints_div_by_both_two_nums(lst):
    result = [num for num in lst[18:53] if num % 15 == 0 and num % 57 == 0]
    if not result:
        return []
    return result