def all_pos_ints_inclusive(integer_list):
    if len(integer_list) < 201:
        return [num for num in integer_list[50:201] if num > 0]
    else:
        return [num for num in integer_list[50:201] if num > 0]