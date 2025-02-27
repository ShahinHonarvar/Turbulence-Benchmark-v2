def find_second_largest_num(num_list):
    return sorted(num_list[15:52])[-2] if len(num_list[15:52]) > 1 else None