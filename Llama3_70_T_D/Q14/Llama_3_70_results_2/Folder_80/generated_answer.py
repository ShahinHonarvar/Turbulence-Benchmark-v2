def find_second_smallest_num(num_list):
    if 87 < len(num_list):
        temp_list = sorted(num_list[30:88])
        if len(temp_list) > 1 and temp_list[0] != temp_list[1]:
            return temp_list[1]
    return None