def find_second_smallest_num(num_list):
    target_list = sorted(num_list[50:55])
    return target_list[1] if len(target_list) > 1 else None