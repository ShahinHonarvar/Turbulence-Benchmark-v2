def find_second_smallest_num(nums):
    if len(nums) < 80 or len(nums) > 90:
        return None
    nums = sorted(nums[75:90])
    return nums[1] if len(nums) >= 2 else None