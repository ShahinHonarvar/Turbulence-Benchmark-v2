def find_second_largest_num(num_list):
    if len(num_list) < 95:
        return None
    selected_nums = num_list[75:95]
    selected_nums.sort(reverse=True)
    if len(selected_nums) < 2:
        return None
    return selected_nums[1]