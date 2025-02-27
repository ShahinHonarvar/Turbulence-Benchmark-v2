def find_second_smallest_num(num_list):
    temp_list = num_list[64:67]
    temp_list.sort()
    return temp_list[1] if len(temp_list) > 1 else None