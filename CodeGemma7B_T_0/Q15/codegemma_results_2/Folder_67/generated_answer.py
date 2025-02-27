def sum_odd_ints_inclusive(nums):
    if not nums or len(nums) < 22 or len(nums) < 50:
        return 0
    sum_odd = 0
    for i in range(22, 51):
        if i % 2 != 0:
            sum_odd += nums[i]
    return sum_odd