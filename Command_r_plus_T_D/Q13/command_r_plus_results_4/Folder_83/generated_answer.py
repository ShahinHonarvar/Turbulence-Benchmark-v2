def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 91:
        return None
    num_list_subset = num_list[90:91]
    if len(num_list_subset) < 2:
        return None
    num_list_subset.sort()
    return num_list_subset[1]