def find_second_largest_num(num_list):
    if len(num_list) < 5:
        return None
    temp_list = num_list[4:5]
    if len(temp_list) < 2:
        return None
    temp_list.sort()
    return temp_list[-2]