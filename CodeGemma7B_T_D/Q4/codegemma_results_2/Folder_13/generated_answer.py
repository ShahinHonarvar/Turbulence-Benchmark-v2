def all_pos_ints_exclusive(int_list):
    result = []
    for num in int_list:
        if num > 0 and num >= 73 and (num < 84):
            result.append(num)
    return result