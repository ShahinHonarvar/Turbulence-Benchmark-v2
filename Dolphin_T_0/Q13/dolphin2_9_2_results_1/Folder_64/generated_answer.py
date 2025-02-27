def find_second_largest_num(lst):
    new_list = lst[0:5]
    if len(new_list) < 2:
        return None
    max_num = max(new_list)
    new_list.remove(max_num)
    second_max = max(new_list)
    return second_max