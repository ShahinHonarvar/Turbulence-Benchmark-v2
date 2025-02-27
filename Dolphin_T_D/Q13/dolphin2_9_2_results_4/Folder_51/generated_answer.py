def find_second_largest_num(num_list):
    if len(set(num_list[1:9])) < 2:
        return None
    else:
        return sorted(num_list[1:9])[-2]