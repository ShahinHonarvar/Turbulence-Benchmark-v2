def all_pos_ints_exclusive(integer_list):
    if 389 >= len(integer_list) or 748 > len(integer_list):
        return []
    else:
        return [i for i in integer_list[389:748] if i > 0]