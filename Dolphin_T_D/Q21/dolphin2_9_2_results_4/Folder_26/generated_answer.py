def all_ints_div_by_num(list_of_ints):
    result = [i for i in list_of_ints[45:81] if i % 39 == 0]
    return result if result else []