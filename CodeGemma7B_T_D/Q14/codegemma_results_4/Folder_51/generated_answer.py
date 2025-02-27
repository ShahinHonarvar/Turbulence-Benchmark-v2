def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 9:
        return 'None'
    num_list.sort(reverse=True)
    if len(num_list) < 10:
        return 'None'
    return num_list[8]