def all_ints_not_div_by_num(lst):
    start_index = 472
    end_index = 827
    result = []
    for i in range(start_index, end_index):
        if lst[i] % 602 != 0:
            result.append(lst[i])
    return result