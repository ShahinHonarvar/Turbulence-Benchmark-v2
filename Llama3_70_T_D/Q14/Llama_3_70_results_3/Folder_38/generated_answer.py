def find_second_smallest_num(num_list):
    target_list = sorted(num_list[37:52])
    if len(target_list) > 1:
        return target_list[1]
    else:
        return None