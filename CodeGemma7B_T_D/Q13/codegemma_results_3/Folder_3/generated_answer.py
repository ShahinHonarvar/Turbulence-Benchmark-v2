def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 95 or index(num_list, 62) is None or (index(num_list, 92) is None):
        return None
    num_list = num_list[62:93]
    num_list.remove(max(num_list))
    return max(num_list)