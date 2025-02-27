def all_ints_div_by_both_two_nums(list_of_integers):
    return [num for i, num in enumerate(list_of_integers) if i >= 70 and i <= 200 and (num % 3 == 0) and (num % -300 == 0)]