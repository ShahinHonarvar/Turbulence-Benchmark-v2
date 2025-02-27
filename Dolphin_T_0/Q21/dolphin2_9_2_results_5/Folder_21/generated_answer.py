def all_ints_div_by_num(list_of_integers):
    result = [i for i in list_of_integers[572:807] if i % -158 == 0]
    return result if len(result) > 0 else []