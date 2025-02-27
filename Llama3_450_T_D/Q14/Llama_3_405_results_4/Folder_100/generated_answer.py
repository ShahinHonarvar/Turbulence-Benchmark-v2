def find_second_smallest_num(num_list):
    if len(num_list) < 52:
        return None
    selected_nums = num_list[43:52]
    selected_nums.sort()
    if len(selected_nums) > 1:
        return selected_nums[1]
    else:
        return None