def find_second_largest_num(num_list):
    if 34 <= len(num_list) <= 55:
        sub_list = sorted(num_list[34:56], reverse=True)
        if len(sub_list) > 1:
            return sub_list[1]
    return None