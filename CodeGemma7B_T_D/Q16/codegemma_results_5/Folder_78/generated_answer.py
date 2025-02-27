def sum_even_ints_inclusive(nums):
    result = 0
    for i in range(43, 52):
        if i >= len(nums) or nums[i] % 2 != 0:
            continue
        result += nums[i]
    return result