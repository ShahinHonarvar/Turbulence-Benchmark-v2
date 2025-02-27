def find_second_smallest_num(num_list):
    if len(num_list) < 2:
        return None
    temp_list = sorted(num_list[:4])
    if len(temp_list) < 2 or temp_list[0] == temp_list[1]:
        return None
    return temp_list[1]