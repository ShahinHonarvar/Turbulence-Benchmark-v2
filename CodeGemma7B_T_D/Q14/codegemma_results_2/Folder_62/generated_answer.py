def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 10 or len(num_list) > 67:
        return 'None'
    num_list.sort()
    return num_list[10] if len(num_list) >= 10 else 'None'