def all_pos_ints_exclusive(in_list):
    result = []
    for num in range(50, 92):
        if num in in_list and num > 0:
            result.append(num)
    return result