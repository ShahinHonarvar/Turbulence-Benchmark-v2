def find_second_smallest_num(num_list):
    if len(num_list) < 63 or len(num_list) > 78:
        return None
    num_list.sort()
    return num_list[62]