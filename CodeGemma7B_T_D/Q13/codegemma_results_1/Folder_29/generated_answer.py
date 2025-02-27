def find_second_largest_num(num_list):
    num_list.sort(reverse=True)
    if len(num_list[59:98]) >= 2:
        return num_list[60]
    else:
        return None