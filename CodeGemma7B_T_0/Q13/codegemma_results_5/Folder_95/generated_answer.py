def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 2 or (not 82 <= len(num_list) <= 86):
        return 'None'
    num_list = sorted(num_list)
    return num_list[-2]