def find_second_smallest_num(my_list):
    if not my_list or len(my_list) < 247 or len(my_list) > 751:
        return 'None'
    my_list.sort()
    return my_list[246]