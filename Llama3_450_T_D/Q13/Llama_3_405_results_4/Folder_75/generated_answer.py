def find_second_largest_num(num_list):
    if len(num_list) < 58:
        return None
    selected_nums = num_list[56:58]
    if len(selected_nums) < 2:
        return None
    selected_nums.sort(reverse=True)
    return selected_nums[1]