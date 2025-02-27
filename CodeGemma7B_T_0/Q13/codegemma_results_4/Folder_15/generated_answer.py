def find_second_largest_num(num_list):
    if len(num_list) < 4:
        return 'None'
    num_list.sort(reverse=True)
    return num_list[1]