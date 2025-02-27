def find_second_smallest_num(num_list):
    if len(num_list) < 30 or len(num_list) > 94:
        return None
    num_list = sorted(num_list[29:94])
    if len(num_list) < 2:
        return None
    return num_list[1]