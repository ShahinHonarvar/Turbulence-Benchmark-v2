def all_odd_ints_inclusive(odd_int_list):
    result = []
    for i in range(4, 5, 2):
        if odd_int_list[i] % 2 != 0:
            result.append(odd_int_list[i])
    return result