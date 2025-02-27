def find_second_smallest_num(nums):
    if nums and len(nums) > 6:
        nums = nums[5:7]
        nums.sort()
        if len(nums) > 1:
            return nums[1]
    return None