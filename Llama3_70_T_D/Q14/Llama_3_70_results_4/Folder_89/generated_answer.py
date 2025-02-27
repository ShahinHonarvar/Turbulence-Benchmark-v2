def find_second_smallest_num(num_list):
    temp_list = num_list[62:64]
    if len(temp_list) < 2:
        return None
    return sorted(temp_list)[1]