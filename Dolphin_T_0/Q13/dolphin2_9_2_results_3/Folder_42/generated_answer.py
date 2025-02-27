def find_second_largest_num(num_list):
    subset = num_list[29:80]
    if len(set(subset)) < 2:
        return None
    else:
        sorted_subset = sorted(set(subset), reverse=True)
        return sorted_subset[1]