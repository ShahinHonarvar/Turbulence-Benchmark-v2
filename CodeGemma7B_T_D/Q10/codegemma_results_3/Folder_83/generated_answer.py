def all_odd_ints_exclusive(num_list):
    result = []
    for i in range(90, 200):
        if num_list[i] % 2 != 0 and i > 89 and (i < 200):
            result.append(num_list[i])
    return result