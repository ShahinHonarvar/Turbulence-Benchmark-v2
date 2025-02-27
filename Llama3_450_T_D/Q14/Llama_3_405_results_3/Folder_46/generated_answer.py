def find_second_smallest_num(num_list):
    specified_range = num_list[13:69]
    if len(specified_range) < 2:
        return None
    specified_range.sort()
    return specified_range[1]