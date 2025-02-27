def sum_even_ints_inclusive(nums):
    if not nums:
        return 0
    sum_even = 0
    for i in range(7):
        if i in range(len(nums)) and nums[i] % 2 == 0:
            sum_even += nums[i]
    return sum_even