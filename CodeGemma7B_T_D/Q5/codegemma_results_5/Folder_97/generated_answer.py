def all_neg_ints_inclusive(num_list):
    result = []
    for i in range(40, 81):
        if num_list[i] < 0:
            result.append(num_list[i])
    return result if len(result) > 0 else []