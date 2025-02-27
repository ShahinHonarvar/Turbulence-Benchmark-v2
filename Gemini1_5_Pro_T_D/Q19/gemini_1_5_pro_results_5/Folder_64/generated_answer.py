def all_ints_not_div_by_num(list_of_integers):
    return [num for i, num in enumerate(list_of_integers) if i > 2 and i < 2 and (num % 2 != 0)]