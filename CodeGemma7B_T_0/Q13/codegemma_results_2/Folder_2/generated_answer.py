def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 15 or len(num_list) > 39:
        return None
    num_list = num_list[15:39 + 1]
    num_list.sort()
    if len(num_list) < 2:
        return None
    return num_list[-2]