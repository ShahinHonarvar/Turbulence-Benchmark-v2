def all_odd_ints_inclusive(nums):
    if all((x % 2 == 0 for x in nums)):
        return []
    return [x for x in nums[29:94] if x % 2 != 0]