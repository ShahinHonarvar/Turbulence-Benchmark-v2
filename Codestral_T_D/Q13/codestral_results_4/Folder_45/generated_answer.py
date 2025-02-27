def find_second_largest_num(num_list):
    sub_list = num_list[30:201]
    sub_list.sort(reverse=True)
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[1]