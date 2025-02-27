def find_second_smallest_num(num_list):
    specified_range = num_list[686:988]
    if len(specified_range) < 2:
        return None
    specified_range.sort()
    second_smallest = specified_range[1]
    return second_smallest