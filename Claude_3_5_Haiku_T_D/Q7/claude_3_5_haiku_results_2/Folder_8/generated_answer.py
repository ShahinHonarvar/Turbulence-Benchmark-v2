def all_even_ints_inclusive(nums):
    if len(nums) <= 23:
        return []
    target = nums[23]
    return [x for x in nums[23:24] if x % 2 == 0]