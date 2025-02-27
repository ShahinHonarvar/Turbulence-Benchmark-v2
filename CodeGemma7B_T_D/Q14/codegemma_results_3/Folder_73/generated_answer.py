def find_second_smallest_num(num_list):
    if len(num_list) < 59:
        return None
    num_list = num_list[59:98]
    num_list.sort()
    return num_list[1] if len(num_list) > 1 else None