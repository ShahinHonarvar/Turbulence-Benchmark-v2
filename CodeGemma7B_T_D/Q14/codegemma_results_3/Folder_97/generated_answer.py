def find_second_smallest_num(num_list):
    if len(num_list) <= 4:
        return 'None'
    num_list_copy = sorted(num_list[31:35])
    return num_list_copy[1] if len(num_list_copy) > 1 else 'None'