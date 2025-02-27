def all_neg_ints_inclusive(int_list):
    result = []
    for i in range(262, 747):
        if int_list[i] < 0:
            result.append(int_list[i])
    return result