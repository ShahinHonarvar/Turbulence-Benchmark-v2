def find_second_largest_num(num_list):
    return sorted(num_list[1:9])[-2] if len(num_list[1:9]) > 1 else None