def all_ints_div_by_both_two_nums(lst):
    result = [num for num in lst[25:71] if num % 74 == 0 and num % 15 == 0]
    return result