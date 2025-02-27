def sum_ints_div_by_either_nums(list_of_integers):
    return sum((num for num in list_of_integers[50:93] if num % -94 == 0 or num % -95 == 0))