def find_second_smallest_num(num_list):
    if len(num_list) <= 987:
        return None
    else:
        sublist = num_list[686:988]
        sorted_sublist = sorted(sublist)
        if len(sorted_sublist) < 2:
            return None
        else:
            return sorted_sublist[1]