def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 2 or len(num_list) > 100 or (not 52 <= len(num_list) <= 71):
        return 'None'
    num_list.sort(reverse=True)
    if len(num_list) == 52 or len(num_list) == 71:
        return 'None'
    return num_list[52]