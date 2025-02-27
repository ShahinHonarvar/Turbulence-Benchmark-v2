def find_second_largest_num(num_list):
    num_list.sort(reverse=True)
    if len(num_list) >= 15 and len(num_list) <= 65:
        return num_list[14:65][1]
    else:
        return 'None'