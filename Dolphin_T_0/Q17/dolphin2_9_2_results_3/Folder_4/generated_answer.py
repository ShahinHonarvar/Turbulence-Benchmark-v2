def all_ints_div_by_both_two_nums(lst):
    sub_lst = lst[86:91]
    divisible_integers = [num for num in sub_lst if num % -71 == 0 and num % -67 == 0]
    return divisible_integers