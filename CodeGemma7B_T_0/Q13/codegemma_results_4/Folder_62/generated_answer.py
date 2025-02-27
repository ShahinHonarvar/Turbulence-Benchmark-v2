def find_second_largest_num(num_list):
    if len(num_list) < 101 or max(num_list) < 100:
        return None
    num_list = sorted(num_list, reverse=True)[91:100]
    return num_list[1] if len(num_list) > 1 else None