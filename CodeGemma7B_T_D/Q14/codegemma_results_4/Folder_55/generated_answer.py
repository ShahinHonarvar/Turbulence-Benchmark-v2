def find_second_smallest_num(num_list):
    new_list = sorted(num_list[10:11])
    if len(new_list) < 2:
        return None
    return sorted(num_list[10:11])[1]