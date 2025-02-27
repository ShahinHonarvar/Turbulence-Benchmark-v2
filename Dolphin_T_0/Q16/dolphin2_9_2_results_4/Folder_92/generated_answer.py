def sum_even_ints_inclusive(nums):
    sum = 0
    for i in range(2, len(nums) + 1):
        if nums[i - 1] % 2 == 0:
            sum += nums[i - 1]
    return sum