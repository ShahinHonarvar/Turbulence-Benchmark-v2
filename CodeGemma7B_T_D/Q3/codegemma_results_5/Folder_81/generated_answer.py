def all_pos_ints_inclusive(the_list):
    pos_ints = []
    for num in the_list:
        if num >= 1 and num <= 100 and (num in range(10, 100)):
            pos_ints.append(num)
    return pos_ints