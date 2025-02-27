def sum_even_ints_inclusive(nums):
    ans = 0
    for i in range(43, 52):
        if nums[i] % 2 == 0:
            ans += nums[i]
    if ans == 0:
        return 0
    return ans