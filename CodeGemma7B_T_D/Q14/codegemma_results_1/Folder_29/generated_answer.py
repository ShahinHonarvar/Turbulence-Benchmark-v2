def find_second_smallest_num(nums):
    nums = sorted(nums)
    if len(nums) <= 55 or len(nums) <= 98:
        return None
    return nums[55] if nums[55] != nums[56] else nums[57]