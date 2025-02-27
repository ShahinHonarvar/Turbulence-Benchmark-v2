def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 86:
        return None
    num_list = sorted(num_list[75:86])
    return num_list[1]