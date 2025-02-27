def find_second_smallest_num(num_list):
    if 246 >= len(num_list) or 750 >= len(num_list):
        return None
    sliced_list = sorted(num_list[246:751])
    if len(sliced_list) < 2:
        return None
    return sliced_list[1]