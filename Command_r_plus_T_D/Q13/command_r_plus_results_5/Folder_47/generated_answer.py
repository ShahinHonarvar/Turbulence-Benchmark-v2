def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    if len(num_list) < 77:
        return None
    relevant_nums = num_list[37:77]
    relevant_nums.sort()
    if len(relevant_nums) < 2:
        return None
    return relevant_nums[-2]