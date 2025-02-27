def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 86:
        return None
    filtered_list = sorted(num_list[82:87], reverse=True)
    if len(filtered_list) < 2:
        return None
    return filtered_list[1]