def all_pos_ints_inclusive(list_of_ints):
    sublist = list_of_ints[6:9]
    pos_list = [i for i in sublist if i > 0]
    return pos_list