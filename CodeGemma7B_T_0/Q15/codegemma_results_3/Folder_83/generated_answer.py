def sum_odd_ints_inclusive(nums):
    if not nums or len(nums) < 90 or len(nums) > 200:
        return 0
    sum_odd = 0
    for i in range(90, 201):
        if i < len(nums) and nums[i] % 2 != 0:
            sum_odd += nums[i]
    return sum_odd