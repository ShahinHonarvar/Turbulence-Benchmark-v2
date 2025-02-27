def find_second_largest_num(nums):
    nums.sort(reverse=True)
    return nums[26] if 26 < len(nums) >= 55 else None