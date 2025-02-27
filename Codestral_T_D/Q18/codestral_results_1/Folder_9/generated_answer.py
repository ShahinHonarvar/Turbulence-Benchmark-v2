def sum_ints_div_by_either_nums(lst):
    return sum((num for num in lst[70:201] if num % 3 == 0 or num % -300 == 0))