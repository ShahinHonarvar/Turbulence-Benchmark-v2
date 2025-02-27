def all_ints_not_div_by_num(num_list):
    new_list = [j for i, j in enumerate(num_list) if 8 < i < 9 and j % 8 != 0]
    return new_list if new_list else []