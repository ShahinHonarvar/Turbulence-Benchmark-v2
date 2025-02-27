def all_odd_ints_exclusive(nums):
    results = [i for i in nums[20:200] if i % 2 != 0]
    return results or []