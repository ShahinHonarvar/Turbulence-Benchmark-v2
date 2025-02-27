def find_second_largest_num(num_list):
    if len(num_list) >= 35:
        subset = num_list[31:35]
        subset.sort(reverse=True)
        return subset[1]
    else:
        return None