def find_second_smallest_num(num_list):
    temp_list = num_list[5:8]
    if len(temp_list) < 2:
        return None
    else:
        temp_list.sort()
        return temp_list[1]