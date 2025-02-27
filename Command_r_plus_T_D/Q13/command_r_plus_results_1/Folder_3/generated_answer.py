def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 93:
        return None
    else:
        num_list_subset = num_list[62:93]
        num_list_subset.sort()
        return num_list_subset[-2]