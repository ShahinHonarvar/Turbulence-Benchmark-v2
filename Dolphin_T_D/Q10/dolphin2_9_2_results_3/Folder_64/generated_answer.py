def all_odd_ints_exclusive(a_list):
    result = []
    for i in range(1, len(a_list) - 1):
        if a_list[i] % 2 != 0:
            result.append(a_list[i])
    return result