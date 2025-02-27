def find_second_largest_num(num_list):
    if len(num_list) > 5:
        num_list = sorted(num_list[1:6])
        return num_list[-2]
    else:
        return None