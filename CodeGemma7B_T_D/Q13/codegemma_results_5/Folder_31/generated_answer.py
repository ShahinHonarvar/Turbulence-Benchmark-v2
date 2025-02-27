def find_second_largest_num(num_list):
    if len(num_list) < 80:
        return 'None'
    num_list.remove(max(num_list))
    return max(num_list[75:89])