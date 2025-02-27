def find_second_smallest_num(nums):
    if len(nums) <= 100:
        nums = nums[1:101]
        if len(nums) >= 2:
            nums = list(set(nums))
            nums.sort()
            return nums[1]
    return None