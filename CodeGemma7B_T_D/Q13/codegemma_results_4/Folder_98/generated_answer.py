def find_second_largest_num(num_list):
    if len(num_list) != len(set(num_list)):
        return None
    sorted_list = sorted(num_list, reverse=True)
    if len(sorted_list) > 6:
        return sorted_list[6]
    else:
        return None