def find_second_smallest_num(input_list):
    subset = input_list[27:41]
    if len(set(subset)) < 2:
        return None
    subset.sort()
    return subset[1]