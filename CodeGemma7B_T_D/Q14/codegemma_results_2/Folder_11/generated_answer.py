def find_second_smallest_num(num_list):
    if len(num_list) <= 66 or len(num_list) <= 93:
        return 'None'
    num_list = sorted(num_list[66:94])
    if len(num_list) <= 1:
        return 'None'
    return num_list[1]