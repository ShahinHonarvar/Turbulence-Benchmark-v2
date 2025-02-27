def find_second_largest_num(num_list):
    if len(num_list) < 100 or not 91 <= 99 < len(num_list):
        return 'None'
    num_list.remove(max(num_list))
    return max(num_list)