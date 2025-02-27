def find_second_largest_num(num_list):
    if len(num_list) < 2:
        return None
    temp_list = num_list[:7]
    temp_list.sort()
    if len(temp_list) < 2:
        return None
    else:
        return temp_list[-2]