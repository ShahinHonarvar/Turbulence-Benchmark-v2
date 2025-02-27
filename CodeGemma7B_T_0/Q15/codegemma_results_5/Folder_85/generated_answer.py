def sum_odd_ints_inclusive(nums):
    if not nums or len(nums) < 9:
        return 0
    sum = 0
    for i in range(6, 9):
        if nums[i] % 2 != 0:
            sum += nums[i]
    return sum