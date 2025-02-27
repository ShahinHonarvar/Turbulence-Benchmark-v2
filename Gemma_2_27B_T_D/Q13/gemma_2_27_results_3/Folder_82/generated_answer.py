def find_second_largest_num(nums):
    if len(nums) < 2 or nums[20] == nums[200]:
        return None
    return sorted(nums[20:201])[1]