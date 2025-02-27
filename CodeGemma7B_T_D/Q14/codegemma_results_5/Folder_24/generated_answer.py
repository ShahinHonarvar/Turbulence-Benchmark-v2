def find_second_smallest_num(num_list):
    if len(num_list) < 25 or not set(sorted(num_list)) == set(range(min(num_list), max(num_list) + 1)):
        return None
    num_list = num_list[23:25]
    return sorted(num_list)[1]