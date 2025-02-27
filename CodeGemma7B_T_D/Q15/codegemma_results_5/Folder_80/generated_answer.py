def sum_odd_ints_inclusive(nums):
    sum = 0
    if len(nums) < 65 or len(nums) > 66:
        return 0
    for i in range(64, 67):
        if nums[i] % 2 != 0:
            sum += nums[i]
    return sum