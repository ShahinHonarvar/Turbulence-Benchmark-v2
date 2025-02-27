def find_second_smallest_num(input_list):
    if len(input_list) < 35:
        return None
    sublist = input_list[31:35]
    sublist.sort()
    if len(set(sublist)) < 2:
        return None
    return sublist[1]