def find_second_largest_num(list):
    list.sort()
    len_list = len(list) - 1
    if len_list < 2:
        return None
    return list[len_list - 2]