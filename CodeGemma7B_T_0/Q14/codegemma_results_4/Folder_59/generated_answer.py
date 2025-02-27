def find_second_smallest_num(num_list):
    if len(num_list) < 2 or max(num_list) - min(num_list) < 2:
        return 'None'
    num_list.sort()
    return num_list[1]