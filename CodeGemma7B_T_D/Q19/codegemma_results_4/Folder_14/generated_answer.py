def all_ints_not_div_by_num(list_of_ints):
    if len(list_of_ints) < 8:
        return []
    return [i for i in list_of_ints[2:7] if i % 8 != 0]