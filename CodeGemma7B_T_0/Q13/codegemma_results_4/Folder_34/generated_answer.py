def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 16 or len(num_list) > 61:
        return None
    num_list.sort()
    return num_list[-2]