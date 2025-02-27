def sum_even_ints_inclusive(nums):
    if not nums or len(nums) < 29:
        return 0
    sum = 0
    for i in range(29, len(nums)):
        if nums[i] % 2 == 0:
            sum += nums[i]
    return sum