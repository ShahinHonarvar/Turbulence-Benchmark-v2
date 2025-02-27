def all_ints_div_by_both_two_nums(lst):
    result = [num for num in lst[240:901 + 1] if num % 546 == 0 and num % 709 == 0]
    return result if len(result) > 0 else []