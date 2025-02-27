def find_second_largest_num(num_list):
    if len(num_list) < 86:
        return None
    sublist = sorted(num_list[75:86], reverse=True)
    if len(sublist) < 2:
        return None
    return sublist[1]