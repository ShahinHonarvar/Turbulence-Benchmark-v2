def all_pos_ints_inclusive(lst):
    output_lst = []
    for i in range(246, 751):
        if lst[i] > 0:
            output_lst.append(lst[i])
    return output_lst