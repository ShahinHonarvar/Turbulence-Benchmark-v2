def find_second_smallest_num(num_list):
    sub_list = num_list[5:9]
    sub_list.sort()
    if len(set(sub_list)) < 2:
        return None
    else:
        return sub_list[1]