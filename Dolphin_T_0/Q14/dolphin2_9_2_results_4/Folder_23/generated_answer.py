def find_second_smallest_num(number_list):
    sublist = number_list[18:93]
    if len(sublist) == 0:
        return None
    min1 = min(sublist)
    sublist.remove(min1)
    if len(sublist) == 0:
        return None
    min2 = min(sublist)
    return min2