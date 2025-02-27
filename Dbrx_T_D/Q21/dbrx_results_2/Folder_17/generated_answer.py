def all_ints_div_by_num(int_list):
    if len(int_list) >= 36:
        result = [i for i in int_list[32:36] if i % 91 == 0]
        return result
    else:
        return []