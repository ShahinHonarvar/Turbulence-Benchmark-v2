def all_ints_div_by_both_two_nums(lst):
    target_numbers = lst[77:88]
    result = [num for num in target_numbers if num % 23 == 0 and num % 57 == 0]
    return result