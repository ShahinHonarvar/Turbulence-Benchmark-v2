def find_second_smallest_num(num_list):
    if len(num_list) < 2 or len(num_list) > 10:
        return None
    num_list.sort()
    if num_list[1] == num_list[0]:
        return None
    return num_list[1]