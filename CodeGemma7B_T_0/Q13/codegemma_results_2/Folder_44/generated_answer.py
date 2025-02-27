def find_second_largest_num(num_list):
    if len(num_list) < 14 or len(num_list) > 69:
        return 'None'
    num_list.sort(reverse=True)
    if num_list[13] == num_list[14]:
        return 'None'
    return num_list[13]