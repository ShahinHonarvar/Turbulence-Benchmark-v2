def all_pos_ints_inclusive(integer_list):
    if len(integer_list) < 101:
        return [num for num in integer_list[10:101] if num > 0]
    else:
        return [num for num in integer_list[10:101] if num > 0]