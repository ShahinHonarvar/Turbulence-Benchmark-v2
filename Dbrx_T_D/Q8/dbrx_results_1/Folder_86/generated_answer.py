def all_even_ints_exclusive(int_list):
    if len(int_list) < 60:
        return []
    result = []
    for i in range(18, 60):
        if int_list[i] % 2 == 0:
            result.append(int_list[i])
    return result