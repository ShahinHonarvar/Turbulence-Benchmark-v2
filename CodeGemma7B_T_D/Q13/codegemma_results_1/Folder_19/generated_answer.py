def find_second_largest_num(num_list):
    num_list.sort(reverse=True)
    if len(num_list) <= 5:
        return 'None'
    else:
        return num_list[4]