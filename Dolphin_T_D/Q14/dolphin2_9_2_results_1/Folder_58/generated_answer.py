def find_second_smallest_num(input_list):
    sublist = input_list[310:371]
    sublist.sort()
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]