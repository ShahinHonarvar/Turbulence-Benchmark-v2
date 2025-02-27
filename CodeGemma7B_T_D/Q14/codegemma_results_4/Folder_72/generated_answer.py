def find_second_smallest_num(num_list):
    num_list = sorted(num_list)
    if len(num_list) < 90:
        return 'None'
    else:
        return num_list[82:87][1]