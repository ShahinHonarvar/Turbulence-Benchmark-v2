def find_second_smallest_num(num_list):
    if len(num_list) < 3 or max(num_list) < 31 or min(num_list) > 72:
        return 'None'
    sorted_list = sorted(num_list[31:73])
    return sorted_list[1] if len(sorted_list) > 1 else 'None'