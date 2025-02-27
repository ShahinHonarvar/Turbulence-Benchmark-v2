def find_second_smallest_num(my_list):
    if 6 < len(my_list) < 7:
        my_list = my_list[6:7]
        if len(my_list) == 1:
            return None
        else:
            my_list.sort()
            return my_list[1]
    else:
        return None