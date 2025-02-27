def all_ints_div_by_both_two_nums(lst):
    divisible = [num for num in lst[240:902] if num % 546 == 0 and num % 709 == 0]
    return divisible or []