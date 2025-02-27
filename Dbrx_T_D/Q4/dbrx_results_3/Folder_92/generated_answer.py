def all_pos_ints_exclusive(int_list):
    if len(int_list) >= 2 and all((isinstance(i, int) for i in int_list)) and (int_list[0] > 0) and (int_list[1] > 0):
        return list(range(int_list[0], int_list[1], 1)) if int_list[0] < int_list[1] else []
    else:
        raise ValueError('Input list must contain at least two positive integers.')