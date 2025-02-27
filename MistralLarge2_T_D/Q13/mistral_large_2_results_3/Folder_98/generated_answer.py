def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    nums = nums[:7]
    nums.sort(reverse=True)
    return nums[1] if len(nums) > 1 else None