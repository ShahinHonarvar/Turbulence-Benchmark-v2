def find_second_smallest_num(num_list):
    temp_list = num_list[22:51]
    temp_list.sort()
    if len(temp_list) < 2:
        return None
    return temp_list[1]