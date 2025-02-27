def find_second_largest_num(num_list):
    if len(num_list) < 88:
        return None
    temp_list = num_list[25:88]
    temp_list.sort(reverse=True)
    if len(temp_list) < 2:
        return None
    return temp_list[1]