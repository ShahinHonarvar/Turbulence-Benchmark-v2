def find_second_largest_num(num_list):
    if len(num_list) >= 5:
        return sorted(num_list[1:6])[4]
    else:
        return None