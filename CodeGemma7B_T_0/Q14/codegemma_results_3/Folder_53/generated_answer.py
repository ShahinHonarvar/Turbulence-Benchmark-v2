def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 2 or max(num_list) < 1 or (min(num_list) > 100):
        return 'None'
    num_list.sort()
    return num_list[1]