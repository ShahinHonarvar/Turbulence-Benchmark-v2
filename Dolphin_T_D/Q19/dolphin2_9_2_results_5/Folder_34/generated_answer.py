def all_ints_not_div_by_num(list_of_ints):
    result = [i for i in list_of_ints[60:200] if i % 9 != 0]
    return result if result else []