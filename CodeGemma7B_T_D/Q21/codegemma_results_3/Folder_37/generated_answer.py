def all_ints_div_by_num(user_list):
    new_list = [item for item in user_list[4:4 + 1] if item % 3 == 0]
    return new_list