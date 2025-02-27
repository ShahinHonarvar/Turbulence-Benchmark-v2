def find_second_largest_num(num_list):
    sublist = num_list[100:201]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    if len(sublist) < 2:
        return None
    second_max_num = max(sublist)
    return second_max_num