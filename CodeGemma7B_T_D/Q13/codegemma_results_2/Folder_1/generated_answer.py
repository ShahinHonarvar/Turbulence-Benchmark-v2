def find_second_largest_num(num_list):
    if len(num_list) <= 31 or len(num_list) > 72:
        return 'None'
    num_list.sort(reverse=True)
    if len(num_list) >= 32:
        return num_list[31]
    return 'None'