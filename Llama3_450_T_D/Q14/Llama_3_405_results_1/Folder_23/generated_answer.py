def find_second_smallest_num(num_list):
    if len(num_list) < 20 or len(num_list) < 93:
        return None
    selected_nums = num_list[19:93]
    selected_nums.sort()
    if len(selected_nums) < 2:
        return None
    return selected_nums[1]