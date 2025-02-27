def find_second_largest_num(nums):
    if 15 <= len(nums) <= 39:
        nums = nums[15:40]
        nums.sort(reverse=True)
        if len(nums) > 1:
            return nums[1]
    return None