def find_second_smallest_num(num_list):
    sub_list = num_list[35:50]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[1]