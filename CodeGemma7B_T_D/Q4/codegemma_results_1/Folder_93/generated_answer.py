def all_pos_ints_exclusive(int_list):
    result = []
    for num in int_list[19:94]:
        if num > 0:
            result.append(num)
    return result