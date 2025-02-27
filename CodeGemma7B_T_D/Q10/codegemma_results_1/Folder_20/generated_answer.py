def all_odd_ints_exclusive(int_list):
    result = []
    for i in range(59, 93):
        if i % 2 != 0:
            result.append(int_list[i])
    return result