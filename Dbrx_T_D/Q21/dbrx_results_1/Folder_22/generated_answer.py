def all_ints_div_by_num(my_list):
    return [i for index, i in enumerate(my_list) if i % 1 == 0 and index >= 10 and (index <= 18)]