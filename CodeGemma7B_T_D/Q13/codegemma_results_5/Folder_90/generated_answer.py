def find_second_largest_num(num_list):
    num_list = sorted(num_list[262:747], reverse=True)
    if len(num_list) > 1:
        return num_list[1]
    else:
        return 'None'