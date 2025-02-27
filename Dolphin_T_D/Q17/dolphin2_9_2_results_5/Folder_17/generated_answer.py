def all_ints_div_by_both_two_nums(lst):
    result = [num for i, num in enumerate(lst) if i >= 81 and i <= 89 and (num % 56 == 0) and (num % 68 == 0)]
    return result