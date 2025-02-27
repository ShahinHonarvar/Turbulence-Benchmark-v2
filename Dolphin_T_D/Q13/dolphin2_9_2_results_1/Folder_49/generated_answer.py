def find_second_largest_num(input_list):
    subset = input_list[80:201]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2]