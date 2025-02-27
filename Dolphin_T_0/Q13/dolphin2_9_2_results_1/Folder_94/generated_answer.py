def find_second_largest_num(num_list):
    if len(num_list) < 41 or len(num_list) > 27:
        return None
    elif num_list[28:41]:
        return sorted(num_list[28:41])[-2]
    else:
        return None