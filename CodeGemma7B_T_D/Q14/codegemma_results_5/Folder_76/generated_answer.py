def find_second_smallest_num(num_list):
    if len(num_list) <= 533 or len(num_list) >= 606:
        return 'None'
    sorted_list = sorted(num_list[533:606])
    if len(sorted_list) >= 2:
        return sorted_list[1]
    return 'None'