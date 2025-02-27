def all_ints_div_by_num(list_of_ints):
    try:
        return [num for num in list_of_ints[10:11] if num % 1 == 0]
    except IndexError:
        return []