def find_second_smallest_num(num_list):
    if len(num_list) >= 9:
        num_list = sorted(num_list[4:9])
        return num_list[1] if len(num_list) > 1 else None
    return None