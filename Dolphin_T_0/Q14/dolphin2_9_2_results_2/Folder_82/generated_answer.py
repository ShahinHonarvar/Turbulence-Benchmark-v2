def find_second_smallest_num(num_list):
    if 20 <= 200 < len(num_list):
        subset_list = num_list[20:201]
        subset_list.sort()
        if len(set(subset_list)) >= 2:
            return subset_list[1]
    return None