def find_second_smallest_num(num_list):
    num_list.sort()
    if len(num_list) <= 9:
        return None
    return num_list[8]