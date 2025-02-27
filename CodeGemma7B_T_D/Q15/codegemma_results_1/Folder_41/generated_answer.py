def sum_odd_ints_inclusive(nums):
    if not nums or len(nums) < 7:
        return 0
    sum = 0
    for i in range(6, len(nums) + 1):
        if i >= 6 and i <= len(nums) and (nums[i] % 2 != 0):
            sum += nums[i]
    return sum