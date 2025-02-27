def find_second_smallest_num(num_list):
    if len(num_list) < 62 or max(num_list) < 57 or min(num_list) > 66:
        return None
    num_list = sorted(num_list[56:67])
    if len(num_list) < 2:
        return None
    return num_list[1]