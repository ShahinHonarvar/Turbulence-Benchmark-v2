def find_second_smallest_num(num_list):
    if len(num_list) < 60:
        return None
    sorted_list = sorted(num_list[60:201])
    return sorted_list[1] if len(sorted_list) > 1 else None