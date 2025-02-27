def find_second_smallest_num(num_list):
    size = len(num_list)
    if size < 3:
        raise ValueError('list should have at least 3 elements')
    num_list.sort()
    return num_list[1] if size > 3 else 'None'