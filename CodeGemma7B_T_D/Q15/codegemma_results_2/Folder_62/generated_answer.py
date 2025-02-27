def sum_odd_ints_inclusive(nums):
    if not nums or len(nums) < 91 or len(nums) > 99:
        return 0
    sum = 0
    for i in range(91, 100):
        if i < len(nums) and nums[i] % 2 != 0:
            sum += nums[i]
    return sum