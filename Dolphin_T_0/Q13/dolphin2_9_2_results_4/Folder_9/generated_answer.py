def find_second_largest_num(n_list):
    if 200 < len(n_list):
        sub_list = n_list[200:201]
        if len(sub_list) > 1:
            sub_list.sort()
            return sub_list[1]
    return None