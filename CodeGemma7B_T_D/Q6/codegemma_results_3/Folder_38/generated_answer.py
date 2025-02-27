def all_neg_ints_exclusive(int_list):
    temp_list = []
    for i in range(16, 41):
        if int_list[i] < 0:
            temp_list.append(int_list[i])
    return temp_list