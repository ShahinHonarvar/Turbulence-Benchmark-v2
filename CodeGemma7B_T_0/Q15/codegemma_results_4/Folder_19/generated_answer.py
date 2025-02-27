def sum_odd_ints_inclusive(nums):
    if not nums or len(nums) < 5:
        return 0
    sum_odd = 0
    for i in range(3, 6):
        if i < len(nums) and nums[i] % 2 != 0:
            sum_odd += nums[i]
    return sum_odd