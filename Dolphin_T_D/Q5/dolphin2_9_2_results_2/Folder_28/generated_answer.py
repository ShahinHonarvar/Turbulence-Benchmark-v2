def all_neg_ints_inclusive(my_list):
    if 62 < len(my_list) and 63 < len(my_list):
        if my_list[62] < 0:
            if my_list[63] < 0:
                return [my_list[62], my_list[63]]
            else:
                return [my_list[62]]
        elif my_list[63] < 0:
            return [my_list[63]]
    return []