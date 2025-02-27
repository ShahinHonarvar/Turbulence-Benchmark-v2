def find_second_smallest_num(input_list):
    if 8 < len(input_list) < 4:
        return None
    sublist = input_list[4:9]
    sublist.sort()
    return sublist[1] if len(sublist) > 1 else None