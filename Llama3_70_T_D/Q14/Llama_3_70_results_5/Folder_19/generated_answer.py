def find_second_smallest_num(num_list):
    sublist = sorted(num_list[4:9])
    if len(sublist) < 2:
        return None
    return sublist[1]