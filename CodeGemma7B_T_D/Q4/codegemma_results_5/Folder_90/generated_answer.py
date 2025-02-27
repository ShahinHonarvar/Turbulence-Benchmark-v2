def all_pos_ints_exclusive(int_list):
    result = []
    for num in range(389, 748):
        if num in int_list:
            result.append(num)
    return result