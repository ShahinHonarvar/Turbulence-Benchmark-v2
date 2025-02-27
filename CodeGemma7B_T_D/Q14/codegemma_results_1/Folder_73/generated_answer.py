def find_second_smallest_num(num_list):
    if len(num_list) <= 58:
        return None
    num_list = sorted(num_list[59:98])
    return num_list[1] if len(num_list) >= 2 else None