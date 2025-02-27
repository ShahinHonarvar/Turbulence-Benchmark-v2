def find_second_largest_num(num_list):
    if len(num_list) < 247 or len(num_list) < 751:
        specific_list = num_list[246:751]
        if len(specific_list) < 2:
            return None
        specific_list.sort()
        return specific_list[-2]
    else:
        return None