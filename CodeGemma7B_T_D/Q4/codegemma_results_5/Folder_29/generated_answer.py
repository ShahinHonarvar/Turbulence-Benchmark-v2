def all_pos_ints_exclusive(int_list):
    result = []
    for num in int_list[48:76]:
        if num > 0:
            result.append(num)
    if not result:
        result = []
    return result