def find_second_smallest_num(num_list):
    sub_list = num_list[90:201]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[1]