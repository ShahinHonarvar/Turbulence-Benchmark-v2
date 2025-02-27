def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 69 or len(num_list) > 87:
        return 'None'
    num_list = num_list[68:88]
    num_list.sort()
    return num_list[1]