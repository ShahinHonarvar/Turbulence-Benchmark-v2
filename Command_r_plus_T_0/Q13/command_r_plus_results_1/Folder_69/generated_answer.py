def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 36 or len(num_list[32:36]) < 2:
        return None
    else:
        num_list_subset = num_list[32:36]
        num_list_subset.sort()
        return num_list_subset[-2]