def find_second_largest_num(nums):
    nums = nums[12:69]
    if len(set(nums)) < 2:
        return None
    first = max(nums)
    nums.remove(first)
    second = max(nums)
    return second