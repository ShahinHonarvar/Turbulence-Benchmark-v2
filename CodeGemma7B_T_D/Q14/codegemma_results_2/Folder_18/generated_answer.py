def find_second_smallest_num(num_list):
    num_list.sort()
    if len(num_list) < 49 or num_list[30] == num_list[48]:
        return None
    return num_list[31]