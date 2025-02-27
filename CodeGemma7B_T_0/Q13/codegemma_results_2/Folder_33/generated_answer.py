def find_second_largest_num(num_list):
    if len(num_list) < 667 or len(num_list) > 774:
        return 'None'
    num_list = sorted(num_list[667:775], reverse=True)
    if len(num_list) < 2:
        return 'None'
    return num_list[1]