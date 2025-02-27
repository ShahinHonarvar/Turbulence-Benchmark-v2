def find_second_smallest_num(num_list):
    num_list = sorted(num_list[20:31])
    return num_list[1] if len(num_list) >= 2 else None