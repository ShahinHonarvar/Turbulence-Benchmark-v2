def all_pos_ints_exclusive(num_list):
    new_list = []
    for i in range(1, 8):
        if i in num_list:
            new_list.append(i)
    return new_list