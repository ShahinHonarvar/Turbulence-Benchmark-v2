def find_second_largest_num(num_list):
    new_list = num_list[0:11]
    new_list.sort()
    if len(new_list) < 2:
        return None
    else:
        return new_list[-2]