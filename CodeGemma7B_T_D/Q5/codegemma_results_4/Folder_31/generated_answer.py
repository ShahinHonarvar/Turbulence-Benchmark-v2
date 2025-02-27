def all_neg_ints_inclusive(int_list):
    result_list = []
    for i in range(75, 89):
        if int_list[i] < 0:
            result_list.append(int_list[i])
    return result_list