def find_second_largest_num(nums):
    if len(nums) < 98:
        return None
    selected_nums = nums[21:98]
    selected_nums.sort(reverse=True)
    if len(selected_nums) < 2:
        return None
    return selected_nums[1]