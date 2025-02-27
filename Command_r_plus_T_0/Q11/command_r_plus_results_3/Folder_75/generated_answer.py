def find_largest_num(num_list):
    if len(num_list) <= 57:
        return None
    else:
        sub_list = num_list[56:58]
        return max(sub_list)