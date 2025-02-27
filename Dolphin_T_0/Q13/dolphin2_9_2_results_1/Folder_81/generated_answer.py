def find_second_largest_num(nums):
    if len(nums) < 10:
        return None
    elif len(nums) < 100:
        nums = nums[10:]
    else:
        nums = nums[10:101]
    if len(set(nums)) < 2:
        return None
    first = max(nums)
    nums.remove(first)
    second = max(nums)
    return second