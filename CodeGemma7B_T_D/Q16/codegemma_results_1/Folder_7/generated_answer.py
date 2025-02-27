def sum_even_ints_inclusive(nums):
    total = 0
    for i in range(661, 925):
        if i % 2 == 0:
            total += nums[i]
    return total if total else 0