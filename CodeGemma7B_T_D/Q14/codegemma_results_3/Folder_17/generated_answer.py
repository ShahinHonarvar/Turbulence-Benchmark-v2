def find_second_smallest_num(num_list):
    num_list = num_list[28:39]
    if len(num_list) < 2:
        return None
    num_list.sort()
    return num_list[1]