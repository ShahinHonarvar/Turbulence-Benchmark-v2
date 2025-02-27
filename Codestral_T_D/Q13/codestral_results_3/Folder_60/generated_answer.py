def find_second_largest_num(num_list):
    num_subset = num_list[75:86]
    if len(num_subset) < 2:
        return None
    num_subset.sort(reverse=True)
    return num_subset[1]