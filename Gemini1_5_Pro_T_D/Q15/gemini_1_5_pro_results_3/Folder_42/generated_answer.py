def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(max(29, len(nums)), min(80, len(nums))):
        if nums[i] % 2 != 0:
            sum += nums[i]
    return sum