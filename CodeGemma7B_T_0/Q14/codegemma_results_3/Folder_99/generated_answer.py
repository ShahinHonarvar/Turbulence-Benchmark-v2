def find_second_smallest_num(num_list):
    if len(num_list) < 609:
        return 'None'
    num_list = sorted(num_list[608:610])
    if len(num_list) < 2:
        return 'None'
    return num_list[1]