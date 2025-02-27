def all_odd_ints_exclusive(int_list):
    result = []
    for i in range(11, 76):
        if i % 2 != 0:
            result.append(int_list[i])
    if not result:
        return []
    return result