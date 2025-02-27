def find_second_largest_num(my_list):
    if len(my_list) < 24 or 24 not in my_list:
        return None
    my_list.sort(reverse=True)
    return my_list[23]