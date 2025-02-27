def find_second_largest_num(nums):
    if not 43 <= len(nums) <= 51:
        return None
    nums.sort(reverse=True)
    return nums[43] if nums[43] != nums[44] else None