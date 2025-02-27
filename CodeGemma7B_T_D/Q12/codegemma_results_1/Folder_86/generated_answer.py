def find_smallest_num(num_list):
    if not num_list or len(num_list) < 74:
        return None
    return min(num_list[66:78])