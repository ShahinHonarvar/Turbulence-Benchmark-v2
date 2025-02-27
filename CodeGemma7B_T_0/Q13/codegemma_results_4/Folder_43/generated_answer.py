def find_second_largest_num(num_list):
    if len(num_list) < 69 or len(num_list) > 87:
        return None
    num_list = sorted(num_list[68:88], reverse=True)
    if len(num_list) < 2:
        return None
    return num_list[1]