def sum_even_ints_inclusive(nums):
    total = 0
    for i in range(len(nums)):
        if i >= 52 and i <= 71 and (nums[i] % 2 == 0):
            total += nums[i]
    return total if total else 0