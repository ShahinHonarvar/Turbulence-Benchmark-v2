def find_second_smallest_num(num_list):
    new_list = sorted(num_list[29:94])
    if len(new_list) < 2:
        return None
    return new_list[1]