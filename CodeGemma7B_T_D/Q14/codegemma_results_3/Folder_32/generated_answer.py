def find_second_smallest_num(num_list):
    num_list.sort()
    if len(num_list) >= 33:
        return num_list[32:36][1]
    else:
        return None