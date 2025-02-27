def find_second_largest_num(num_list):
    sorted_num = sorted(num_list, reverse=True)
    if len(sorted_num) < 37:
        return 'None'
    else:
        return sorted_num[37:52][1]