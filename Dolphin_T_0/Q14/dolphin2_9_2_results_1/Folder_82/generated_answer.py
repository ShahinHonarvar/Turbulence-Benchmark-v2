def find_second_smallest_num(nums):
    if 20 <= len(nums) <= 200:
        nums = nums[20:201]
        if len(nums) >= 2:
            nums.sort()
            return nums[1]
    return None