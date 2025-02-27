def all_ints_div_by_num(list_of_integers):
    if len(list_of_integers) <= 8:
        return []
    else:
        return [num for num in list_of_integers[8:9] if num % 8 == 0]