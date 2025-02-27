def find_second_smallest_num(num_list):
    specified_range = num_list[686:988]
    if len(specified_range) < 2:
        return None
    else:
        return sorted(specified_range)[1]