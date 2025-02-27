def all_even_ints_inclusive(int_list):
    if len(int_list) > 78 or len(int_list) < 37:
        return []
    result = []
    for i in range(37, 77):
        if int_list[i] % 2 == 0:
            result.append(int_list[i])
    return result