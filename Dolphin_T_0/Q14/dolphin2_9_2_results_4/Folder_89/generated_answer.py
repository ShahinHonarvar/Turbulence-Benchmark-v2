def find_second_smallest_num(num_list):
    sublist = num_list[62:64]
    sorted_sublist = sorted(sublist)
    if len(set(sorted_sublist)) == 1:
        return None
    else:
        return sorted_sublist[1]