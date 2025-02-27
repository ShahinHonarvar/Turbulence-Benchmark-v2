def all_neg_ints_inclusive(int_list):
    if len(int_list) <= 774:
        return [i for i in int_list[666:775] if i < 0]
    else:
        return [i for i in int_list[666:775] if i < 0] + [i for i in int_list[774:] if i < 0]