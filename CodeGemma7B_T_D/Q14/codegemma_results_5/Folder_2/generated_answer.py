def find_second_smallest_num(num_list):
    if not num_list:
        return None
    num_list = num_list[43:87]
    num_list.sort()
    return num_list[1]