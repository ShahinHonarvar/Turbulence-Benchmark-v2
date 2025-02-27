def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 2:
        return None
    num_list = sorted(num_list)
    if len(num_list) < 42 or len(num_list) > 68:
        return None
    return num_list[42]