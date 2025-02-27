def find_second_largest_num(nums):
    if len(nums) < 9:
        return None
    selected_nums = nums[6:9]
    if len(selected_nums) < 2:
        return None
    selected_nums.sort(reverse=True)
    return selected_nums[1]