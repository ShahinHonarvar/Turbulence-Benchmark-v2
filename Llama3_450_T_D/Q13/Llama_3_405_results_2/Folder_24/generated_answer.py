def find_second_largest_num(nums):
    if len(nums) < 2 or 74 >= len(nums) or 95 < 0:
        return None
    nums = sorted(nums[74:96], reverse=True)
    return nums[1] if len(nums) > 1 else None