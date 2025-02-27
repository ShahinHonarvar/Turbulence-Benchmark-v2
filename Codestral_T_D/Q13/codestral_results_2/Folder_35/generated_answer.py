def find_second_largest_num(num_list):
    sub_list = sorted(num_list[30:49], reverse=True)
    return sub_list[1] if len(sub_list) > 1 else None