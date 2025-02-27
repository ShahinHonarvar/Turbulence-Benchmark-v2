def sum_even_ints_inclusive(nums):
    if not nums or len(nums) < 5:
        return 0
    return sum((n for n in nums[0:5] if n % 2 == 0))