def all_pos_ints_exclusive(a_list):
    start = 66
    end = 90
    result = [i for i in a_list[start:end] if i > 0]
    return result