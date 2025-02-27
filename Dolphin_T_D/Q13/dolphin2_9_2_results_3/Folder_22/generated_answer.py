def find_second_largest_num(number_list):
    if 200 < len(number_list) < 40:
        return None
    sublist = number_list[40:201]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    second_max = max(sublist)
    return second_max