def sum_odd_ints_inclusive(nums):
    if not nums or len(nums) < 91:
        return 0
    return sum((x for x in nums[90:201] if x % 2 != 0))