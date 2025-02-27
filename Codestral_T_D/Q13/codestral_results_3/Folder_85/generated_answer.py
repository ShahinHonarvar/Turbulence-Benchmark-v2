def find_second_largest_num(num_list):
    subset = sorted(num_list[6:9], reverse=True)
    if len(subset) < 2:
        return None
    else:
        return subset[1]