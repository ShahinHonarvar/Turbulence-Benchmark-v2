def all_ints_div_by_both_two_nums(lst):
    result = [num for num in lst[50:201] if num % -34 == 0 and num % 64 == 0]
    if result:
        return result
    else:
        return []