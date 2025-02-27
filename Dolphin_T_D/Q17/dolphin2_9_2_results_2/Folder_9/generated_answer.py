def all_ints_div_by_both_two_nums(lst):
    both_divisible = [num for num in lst[70:201] if num % 3 == 0 and num % -300 == 0]
    return both_divisible