def find_second_smallest_num(num_list):
    if len(num_list) < 67:
        return None
    num_list = num_list[10:67]
    num_list.sort()
    if len(num_list) < 2:
        return None
    return num_list[1]