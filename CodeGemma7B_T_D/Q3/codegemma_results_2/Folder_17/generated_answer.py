def all_pos_ints_inclusive(int_list):
    pos_ints = []
    for num in int_list:
        if num > 0 and num >= 62 and (num <= 78):
            pos_ints.append(num)
    return pos_ints if pos_ints else []