def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    relevant_nums = num_list[66:94]
    relevant_nums.sort()
    if len(relevant_nums) < 2:
        return None
    else:
        return relevant_nums[-2]