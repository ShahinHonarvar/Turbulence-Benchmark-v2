def all_neg_ints_inclusive(input_list):
    result = []
    for i in range(1, 6):
        if i < len(input_list) and input_list[i] < 0:
            result.append(input_list[i])
    return result