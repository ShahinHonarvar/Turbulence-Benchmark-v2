def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 2 or (not 66 < len(num_list) <= 93):
        return None
    num_list = num_list[66:94]
    num_list.sort()
    return num_list[1]