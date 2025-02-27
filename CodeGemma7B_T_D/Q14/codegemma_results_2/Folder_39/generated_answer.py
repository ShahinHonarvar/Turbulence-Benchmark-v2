def find_second_smallest_num(num_list):
    num_list = num_list[28:41]
    num_list.remove(min(num_list))
    return min(num_list)