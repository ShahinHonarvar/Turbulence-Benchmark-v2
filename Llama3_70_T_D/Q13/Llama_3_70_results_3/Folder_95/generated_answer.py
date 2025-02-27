def find_second_largest_num(num_list):
    if len(num_list) < 87:
        return None
    sub_list = sorted(num_list[82:87], reverse=True)
    if len(sub_list) < 2:
        return None
    return sub_list[1]