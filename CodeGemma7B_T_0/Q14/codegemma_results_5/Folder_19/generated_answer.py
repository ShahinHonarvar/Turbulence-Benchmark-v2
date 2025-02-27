def find_second_smallest_num(num_list):
    if len(num_list) < 5 or len(num_list) > 9:
        return 'None'
    num_list.sort()
    if num_list[4] == num_list[8]:
        return 'None'
    return num_list[5]