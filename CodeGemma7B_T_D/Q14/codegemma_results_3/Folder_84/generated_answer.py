def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 41:
        return None
    num_list.sort()
    return num_list[40] if num_list[40] != num_list[41] else num_list[41]