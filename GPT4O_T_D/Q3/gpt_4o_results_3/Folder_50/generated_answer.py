def all_pos_ints_inclusive(int_list):
    start_index = 70
    end_index = 84
    positive_integers = []
    if len(int_list) > start_index:
        for i in range(start_index, min(end_index + 1, len(int_list))):
            if int_list[i] > 0:
                positive_integers.append(int_list[i])
    return positive_integers