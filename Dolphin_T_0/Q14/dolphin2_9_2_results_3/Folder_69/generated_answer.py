def find_second_smallest_num(input_list):
    sublist = input_list[25:88]
    sublist = list(set(sublist))
    if len(sublist) < 2:
        return None
    sublist.remove(min(sublist))
    if len(sublist) < 2:
        return None
    return min(sublist)