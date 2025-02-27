def find_second_smallest_num(num_list):
    target_list = sorted(num_list[80:201])
    if len(target_list) < 2:
        return None
    return target_list[1]