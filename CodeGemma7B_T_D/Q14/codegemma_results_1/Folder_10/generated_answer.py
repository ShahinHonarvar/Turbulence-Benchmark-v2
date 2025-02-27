def find_second_smallest_num(num_list):
    min_element = min(num_list)
    num_list.remove(min_element)
    second_min_element = min(num_list)
    return second_min_element