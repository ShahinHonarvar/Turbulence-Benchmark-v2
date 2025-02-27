def find_second_smallest_num(num_list):
    if len(num_list) < 50 or len(num_list) > 55:
        return 'None'
    num_list.sort()
    if num_list[50] == num_list[54]:
        return 'None'
    return num_list[51]