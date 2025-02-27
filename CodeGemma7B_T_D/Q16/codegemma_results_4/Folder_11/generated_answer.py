def sum_even_ints_inclusive(nums):
    ans = 0
    for i in range(37, 52):
        if nums[i] % 2 == 0:
            ans += nums[i]
    return ans or 0