def sum_even_ints_inclusive(nums):
    result = 0
    for i in range(40, 82):
        if i in range(40, 82) and nums[i] % 2 == 0:
            result += nums[i]
    if result == 0:
        return 0
    return result