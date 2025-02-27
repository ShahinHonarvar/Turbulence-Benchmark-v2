def all_ints_div_by_both_two_nums(list_of_integers):
    return [i for i in list_of_integers[0:10] if i % 6 == 0 and i % -3 == 0]