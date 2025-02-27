def all_pos_ints_exclusive(numbers_list):
    lower_bound = 28
    upper_bound = 49
    result = []
    for i in range(lower_bound, upper_bound):
        if i < len(numbers_list) and numbers_list[i] > 0:
            result.append(numbers_list[i])
    return result