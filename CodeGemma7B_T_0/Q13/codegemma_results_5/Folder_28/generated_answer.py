def find_second_largest_num(num_list):
    if len(num_list) < 62 or len(num_list) > 64:
        return 'None'
    num_list = num_list[62:64]
    num_list.sort(reverse=True)
    if len(num_list) < 2:
        return 'None'
    return num_list[1]