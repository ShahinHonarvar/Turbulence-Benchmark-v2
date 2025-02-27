def find_second_smallest_num(num_list):
    num_list.sort()
    if len(num_list) > 42 and len(num_list) != 87:
        return num_list[43:88][1]
    else:
        return None