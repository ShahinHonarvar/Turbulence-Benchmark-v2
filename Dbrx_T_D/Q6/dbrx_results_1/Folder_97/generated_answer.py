def all_neg_ints_exclusive(input_list):
    if len(input_list) < 93:
        return []
    result = []
    for i in range(20, 93):
        if input_list[i] < 0:
            result.append(input_list[i])
    return result