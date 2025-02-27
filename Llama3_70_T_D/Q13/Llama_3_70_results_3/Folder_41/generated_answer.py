def find_second_largest_num(num_list):
    if len(num_list) > 6:
        num_list = num_list[:7]
    num_list.sort(reverse=True)
    if len(num_list) > 1:
        return num_list[1]
    else:
        return None