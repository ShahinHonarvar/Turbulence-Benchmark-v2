def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 95:
        return None
    else:
        num_list_subset = num_list[75:95]
        num_list_subset.sort()
        return num_list_subset[-2]