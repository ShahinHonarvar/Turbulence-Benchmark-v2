def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 110 or max(num_list) - min(num_list) < 100:
        return None
    num_list = sorted(num_list[90:201])
    if len(num_list) < 2:
        return None
    return num_list[1]