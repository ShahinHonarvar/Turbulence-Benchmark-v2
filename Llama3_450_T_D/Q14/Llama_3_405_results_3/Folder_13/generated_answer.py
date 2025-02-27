def find_second_smallest_num(num_list):
    specified_range = num_list[28:33]
    sorted_range = sorted(specified_range)
    if len(sorted_range) < 2:
        return None
    else:
        return sorted_range[1]