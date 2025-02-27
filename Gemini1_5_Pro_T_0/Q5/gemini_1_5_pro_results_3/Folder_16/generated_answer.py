def all_neg_ints_inclusive(input_list):
    neg_ints = []
    for i in range(33, 37):
        if i < len(input_list) and input_list[i] < 0:
            neg_ints.append(input_list[i])
    return neg_ints