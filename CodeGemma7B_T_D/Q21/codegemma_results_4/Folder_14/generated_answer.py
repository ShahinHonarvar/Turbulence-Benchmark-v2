def all_ints_div_by_num(num_list):
    vals_list = [x for x in num_list[8:9] if x % 8 == 0]
    if len(vals_list) == 0:
        return []
    return vals_list