def all_ints_div_by_both_two_nums(lst):
    result = [num for i, num in enumerate(lst[80:201], 80) if num % 10 == 0 and num % 1000 == 0]
    return result if result else []