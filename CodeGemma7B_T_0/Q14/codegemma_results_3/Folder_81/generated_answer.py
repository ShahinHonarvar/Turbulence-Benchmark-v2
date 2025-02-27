def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 11:
        return 'None'
    num_list.sort()
    for i in range(10, 101):
        if i < len(num_list):
            return num_list[i]
    return 'None'