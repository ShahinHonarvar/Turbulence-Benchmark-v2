def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 85:
        return None
    num_list.sort()
    return num_list[70]