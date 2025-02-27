def all_odd_ints_inclusive(nums):
    if not nums or len(nums) < 7:
        return []
    result = [n for n in nums[0:7] if n % 2 != 0]
    if not result:
        return []
    return result