def find_second_largest_num(num_list):
    if len(num_list) < 36 or len(num_list[32:36]) < 2:
        return None
    temp_list = sorted(num_list[32:36], reverse=True)
    return temp_list[1]