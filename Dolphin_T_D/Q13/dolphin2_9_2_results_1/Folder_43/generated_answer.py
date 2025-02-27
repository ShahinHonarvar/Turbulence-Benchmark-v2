def find_second_largest_num(num_list):
    if len(num_list[68:87]) < 2:
        return None
    else:
        sorted_num = sorted(num_list[68:87])
        return sorted_num[-2]