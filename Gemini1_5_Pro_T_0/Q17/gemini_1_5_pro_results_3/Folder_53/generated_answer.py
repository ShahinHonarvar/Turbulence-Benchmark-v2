def all_ints_div_by_both_two_nums(list_of_integers):
    return [integer for integer in list_of_integers[200:201] if integer % 17 == 0 and integer % -5 == 0]