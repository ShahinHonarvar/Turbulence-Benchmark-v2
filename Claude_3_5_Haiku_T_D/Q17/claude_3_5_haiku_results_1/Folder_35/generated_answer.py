def all_ints_div_by_both_two_nums(lst):
    result = [num for num in lst[77:88] if num % 23 == 0 and num % 57 == 0]
    return result