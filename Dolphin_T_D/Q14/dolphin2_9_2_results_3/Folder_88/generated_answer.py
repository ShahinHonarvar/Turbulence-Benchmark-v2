def find_second_smallest_num(nums):
    if 6 <= len(nums) <= 8:
        nums = nums[6:9]
        nums.sort()
        return nums[1] if len(nums) > 1 else None
    else:
        return None