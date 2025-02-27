def find_second_smallest_num(num_list):
    if len(num_list) < 2:
        return None
    num_list.sort()
    return num_list[1] if num_list[1] in range(7) else None