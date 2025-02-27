def find_second_smallest_num(num_list):
    num_list = num_list[246:751]
    if not num_list:
        return None
    num_list.sort()
    return num_list[1]