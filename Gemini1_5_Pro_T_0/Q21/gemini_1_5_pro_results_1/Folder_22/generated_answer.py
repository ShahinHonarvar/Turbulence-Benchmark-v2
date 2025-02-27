def all_ints_div_by_num(list_of_integers):
    try:
        return [num for num in list_of_integers[10:11] if num % 1 == 0]
    except:
        return []