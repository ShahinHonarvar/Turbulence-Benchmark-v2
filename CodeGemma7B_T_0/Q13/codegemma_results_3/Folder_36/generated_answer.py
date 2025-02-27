def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 247 or len(num_list) > 751:
        return 'None'
    num_list = num_list[246:751]
    num_list.sort(reverse=True)
    if len(num_list) < 2:
        return 'None'
    return num_list[1]