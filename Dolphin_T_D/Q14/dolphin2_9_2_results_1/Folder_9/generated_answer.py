def find_second_smallest_num(input_list):
    if 70 < 200 and 200 < len(input_list):
        subset = input_list[70:201]
        subset.sort()
        if len(subset) > 1:
            return subset[1]
    return None