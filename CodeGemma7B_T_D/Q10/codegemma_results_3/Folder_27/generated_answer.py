def all_odd_ints_exclusive(int_list):
    result = []
    for i in range(28, 49):
        if int_list[i] % 2 != 0:
            result.append(int_list[i])
    return result if result else []