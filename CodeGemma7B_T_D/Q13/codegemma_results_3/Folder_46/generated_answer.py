def find_second_largest_num(num_list):
    if 30 <= len(num_list) <= 87:
        num_list.sort()
        return num_list[-2]
    return None