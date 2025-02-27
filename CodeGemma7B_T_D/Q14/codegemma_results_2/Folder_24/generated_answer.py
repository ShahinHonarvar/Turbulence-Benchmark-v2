def find_second_smallest_num(num_list):
    num_list = num_list[23:24]
    num_list.remove(max(num_list))
    return min(num_list) if num_list else 'None'