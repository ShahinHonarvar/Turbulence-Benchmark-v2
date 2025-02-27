def find_second_smallest_num(num_list):
    sub_list = num_list[209:557]
    sub_list.sort()
    if len(sub_list) >= 2:
        return sub_list[1]
    else:
        return None