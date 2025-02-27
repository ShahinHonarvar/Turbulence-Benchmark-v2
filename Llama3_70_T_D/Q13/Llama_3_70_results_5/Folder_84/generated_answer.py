def find_second_largest_num(num_list):
    if len(num_list) < 87:
        return None
    else:
        return sorted(num_list[43:87], reverse=True)[1]