def find_second_largest_num(nums):
    if len(nums[25:88]) < 2:
        return None
    else:
        nums = nums[25:88]
        max_num = max(nums)
        nums.remove(max_num)
        return max(nums)