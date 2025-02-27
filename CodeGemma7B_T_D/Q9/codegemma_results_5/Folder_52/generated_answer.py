def all_odd_ints_inclusive(int_list):
    result = []
    for i in range(28, 39):
        if i < len(int_list) and int_list[i] % 2 != 0:
            result.append(int_list[i])
    return result