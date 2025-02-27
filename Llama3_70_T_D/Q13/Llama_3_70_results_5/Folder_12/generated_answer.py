def find_second_largest_num(num_list):
    temp_list = num_list[14:65]
    temp_list.sort(reverse=True)
    if len(temp_list) < 2:
        return None
    return temp_list[1]