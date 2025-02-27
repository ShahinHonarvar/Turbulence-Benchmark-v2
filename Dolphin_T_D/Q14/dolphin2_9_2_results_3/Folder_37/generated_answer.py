def find_second_smallest_num(lst):
    if len(lst) == 0 or len(lst) < 8 or len(lst) == 1:
        return 'None'
    else:
        new_list = lst[4:8]
        new_list.sort()
        return new_list[1]