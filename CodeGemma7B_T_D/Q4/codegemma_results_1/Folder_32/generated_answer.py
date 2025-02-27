def all_pos_ints_exclusive(num_list):
    result = []
    for num in num_list:
        if num in range(11, 76) and num > 0:
            result.append(num)
    return result