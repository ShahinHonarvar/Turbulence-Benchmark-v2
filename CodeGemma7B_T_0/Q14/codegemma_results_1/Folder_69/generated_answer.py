def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 25 or len(num_list) > 87:
        return 'None'
    num_list.sort()
    return num_list[25]