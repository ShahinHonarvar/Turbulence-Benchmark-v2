def all_ints_div_by_num(int_list):
    if len(int_list) < 5:
        return []
    result = [i for i in int_list[4:5] if i % 3 == 0]
    return result