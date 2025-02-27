def find_second_largest_num(num_list):
    num_list = num_list[66:94]
    num_list.sort()
    if len(num_list) >= 2:
        return num_list[-2]
    else:
        return None