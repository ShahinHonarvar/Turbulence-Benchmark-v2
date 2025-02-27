def all_pos_ints_inclusive(integer_list):
    positive_ints = []
    for i in range(len(integer_list)):
        if integer_list[i] > 0 and i >= 35 and (i <= 49):
            positive_ints.append(integer_list[i])
    return positive_ints