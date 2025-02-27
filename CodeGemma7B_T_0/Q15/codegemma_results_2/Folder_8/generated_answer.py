def sum_odd_ints_inclusive(nums):
    if not nums or len(nums) < 23:
        return 0
    sum = 0
    for i in range(23, len(nums) + 1):
        if i % 2 != 0:
            sum += nums[i - 1]
    return sum