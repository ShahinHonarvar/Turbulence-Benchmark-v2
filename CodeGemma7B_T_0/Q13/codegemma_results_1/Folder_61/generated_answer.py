def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 2 or max(num_list) == min(num_list):
        return 'None'
    num_list.remove(max(num_list))
    return max(num_list)