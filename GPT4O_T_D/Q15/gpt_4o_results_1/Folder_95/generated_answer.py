def sum_odd_ints_inclusive(nums):
    if len(nums) < 87:
        return 0
    return sum((x for x in nums[82:87] if x % 2 != 0))