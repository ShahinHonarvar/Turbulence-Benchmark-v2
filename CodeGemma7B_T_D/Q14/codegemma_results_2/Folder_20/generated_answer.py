def find_second_smallest_num(num_list):
    if len(num_list) < 75 or len(num_list) > 94:
        return 'None'
    num_list.sort()
    if len(num_list) >= 75 and len(num_list) <= 94:
        return num_list[76]
    else:
        return 'None'