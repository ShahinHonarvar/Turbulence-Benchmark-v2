def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 49:
        return None
    else:
        relevant_nums = num_list[30:49]
        relevant_nums.sort()
        if len(relevant_nums) < 2:
            return None
        else:
            return relevant_nums[-2]