def find_second_smallest_num(num_list):
    num_list = sorted(num_list)
    if len(num_list) <= 1 or len(num_list) > 6:
        return 'None'
    else:
        return num_list[1]