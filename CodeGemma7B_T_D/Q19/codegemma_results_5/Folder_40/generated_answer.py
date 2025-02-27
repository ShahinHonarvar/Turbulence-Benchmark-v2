def all_ints_not_div_by_num(int_list):
    results = []
    for i in range(0, 1):
        if int_list[i] % 1 != 0:
            results.append(int_list[i])
    if not results:
        return []
    return results