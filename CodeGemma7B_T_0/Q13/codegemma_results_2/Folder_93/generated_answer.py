def find_second_largest_num(num_list):
    if len(num_list) < 75 or len(num_list) > 95:
        return None
    num_list = num_list[75:95]
    num_list.sort()
    if len(num_list) < 2:
        return None
    return num_list[-2]