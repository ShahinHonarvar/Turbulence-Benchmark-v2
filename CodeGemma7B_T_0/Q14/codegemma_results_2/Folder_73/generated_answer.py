def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 35 or max(num_list) - min(num_list) < 100:
        return None
    num_list = sorted(num_list[59:98])
    return num_list[1] if len(num_list) > 1 else None