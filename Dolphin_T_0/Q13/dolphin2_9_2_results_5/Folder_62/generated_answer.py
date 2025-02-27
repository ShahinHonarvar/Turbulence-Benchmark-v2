def find_second_largest_num(num_list):
    if len(num_list) >= 100 and 91 <= 99 < len(num_list):
        nums_subset = num_list[91:100]
        nums_subset.sort()
        return nums_subset[-2] if len(nums_subset) >= 2 else None
    else:
        return None