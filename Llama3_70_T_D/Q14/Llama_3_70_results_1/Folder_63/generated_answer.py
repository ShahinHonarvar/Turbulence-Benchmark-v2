def find_second_smallest_num(num_list):
    if len(num_list) < 83:
        return None
    subset = sorted(num_list[56:83])
    if len(subset) < 2 or subset[0] == subset[1]:
        return None
    return subset[1]