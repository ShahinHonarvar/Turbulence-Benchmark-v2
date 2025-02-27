def find_second_largest_num(num_list):
    if len(num_list) < 62 or len(num_list) > 78:
        return 'None'
    num_list = sorted(num_list[62:79])
    return num_list[-2]