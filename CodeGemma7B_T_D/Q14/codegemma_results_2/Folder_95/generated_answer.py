def find_second_smallest_num(num_list):
    if not num_list:
        return 'None'
    num_list_sorted = sorted(num_list)
    if len(num_list_sorted) < 76:
        return 'None'
    return num_list_sorted[75]