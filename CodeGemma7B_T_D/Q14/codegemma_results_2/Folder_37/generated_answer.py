def find_second_smallest_num(num_list):
    if len(num_list) == 0:
        return None
    if len(num_list) < 6:
        return None
    num_list = sorted(num_list)
    if num_list[5] == num_list[6]:
        return None
    return num_list[6]