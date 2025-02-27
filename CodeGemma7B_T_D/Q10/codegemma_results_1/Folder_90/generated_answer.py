def all_odd_ints_exclusive(nums):
    if 389 < len(nums) - 1 and len(nums) - 1 < 748:
        return []
    return nums[389 + 1:748] if all((x % 2 for x in nums[389 + 1:748])) else []