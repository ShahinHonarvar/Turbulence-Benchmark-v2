def find_second_largest_num(nums):
    if len(nums) < 101:
        return None
    selected_nums = nums[10:101]
    if len(selected_nums) < 2:
        return None
    selected_nums.sort(reverse=True)
    return selected_nums[1]