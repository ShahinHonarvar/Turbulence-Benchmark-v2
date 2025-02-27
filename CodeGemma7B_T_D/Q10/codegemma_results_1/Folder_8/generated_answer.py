def all_odd_ints_exclusive(num_list):
    result = []
    for i in range(56, 92):
        if num_list[i] % 2 != 0:
            result.append(num_list[i])
    return result