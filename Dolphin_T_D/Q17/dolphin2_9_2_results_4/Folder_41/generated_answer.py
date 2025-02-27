def all_ints_div_by_both_two_nums(lst):
    divisible_lst = [num for num in lst[0:10] if num % 6 == 0 and num % -3 == 0]
    return divisible_lst