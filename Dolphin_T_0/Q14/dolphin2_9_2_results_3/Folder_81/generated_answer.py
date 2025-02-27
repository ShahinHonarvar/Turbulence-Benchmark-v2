def find_second_smallest_num(nums):
    if 10 <= len(nums) <= 100:
        nums = nums[10:101]
        if len(set(nums)) != len(nums):
            return None
        nums.sort()
        return nums[1]
    else:
        return None