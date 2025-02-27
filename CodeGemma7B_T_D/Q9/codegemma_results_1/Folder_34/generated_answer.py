def all_odd_ints_inclusive(num_list):
    if not num_list:
        return []
    result = []
    for i in range(60, 61):
        if num_list[i] % 2 != 0:
            result.append(num_list[i])
    return result