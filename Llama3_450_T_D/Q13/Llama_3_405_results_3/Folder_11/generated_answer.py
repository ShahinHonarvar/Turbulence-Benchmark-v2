def find_second_largest_num(num_list):
    specified_range = num_list[37:52]
    if len(specified_range) < 2:
        return None
    else:
        specified_range.sort(reverse=True)
        return specified_range[1]