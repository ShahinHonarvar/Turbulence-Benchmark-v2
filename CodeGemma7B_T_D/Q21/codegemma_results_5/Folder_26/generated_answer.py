def all_ints_div_by_num(int_list):
    result = [i for i in int_list[45:81] if i % 39 == 0]
    return result or []