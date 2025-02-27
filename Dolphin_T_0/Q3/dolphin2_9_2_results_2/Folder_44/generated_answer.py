def all_pos_ints_inclusive(lst):
    new_list = [num for num in lst[13:69] if num > 0]
    return new_list if len(new_list) > 0 else []