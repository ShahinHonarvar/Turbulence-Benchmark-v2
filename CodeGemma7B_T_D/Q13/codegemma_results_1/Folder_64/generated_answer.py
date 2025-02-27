def find_second_largest_num(num_list):
    if len(num_list) > 4:
        num_list = num_list[:5]
        num_list.sort(reverse=True)
        return num_list[1]
    else:
        return 'None'