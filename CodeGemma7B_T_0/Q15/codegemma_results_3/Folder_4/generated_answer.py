def sum_odd_ints_inclusive(nums):
    if not nums or len(nums) < 12 or len(nums) > 92:
        return 0
    sum_odd = 0
    for i in range(12, 93):
        if i % 2 != 0:
            sum_odd += nums[i]
    return sum_odd