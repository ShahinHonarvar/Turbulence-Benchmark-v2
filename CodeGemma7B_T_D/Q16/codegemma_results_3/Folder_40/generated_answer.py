def sum_even_ints_inclusive(nums):
    total = 0
    for i in range(len(nums)):
        if i in [0, len(nums) - 1]:
            total += nums[i]
        elif nums[i] % 2 == 0:
            total += nums[i]
    return total