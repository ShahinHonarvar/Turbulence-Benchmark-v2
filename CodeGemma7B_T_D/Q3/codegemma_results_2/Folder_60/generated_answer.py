def all_pos_ints_inclusive(int_list):
    return [num for num in int_list[75:86] if int(num) >= 0] if max(int_list[75:86]) >= 0 else []