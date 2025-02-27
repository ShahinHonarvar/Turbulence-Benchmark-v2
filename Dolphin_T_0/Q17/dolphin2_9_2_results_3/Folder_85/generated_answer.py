def all_ints_div_by_both_two_nums(lst):
    result = [num for num in lst[1:9] if num % -9 == 0 and num % -3 == 0]
    if not result:
        return []
    return result