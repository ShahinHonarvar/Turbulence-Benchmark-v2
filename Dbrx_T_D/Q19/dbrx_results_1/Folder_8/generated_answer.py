def all_ints_not_div_by_num(integer_list):
    return [i for i in integer_list if i % -75 != 0 and 17 <= integer_list.index(i) < 88]