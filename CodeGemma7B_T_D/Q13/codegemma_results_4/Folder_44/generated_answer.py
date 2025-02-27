def find_second_largest_num(num_list):
    num_list = sorted(num_list[13:69], reverse=True)
    if len(num_list) == 0:
        return None
    elif len(num_list) == 1:
        return None
    else:
        return num_list[1]