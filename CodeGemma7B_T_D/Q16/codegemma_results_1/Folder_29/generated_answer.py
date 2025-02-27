def sum_even_ints_inclusive(nums):
    ind_start = 59
    ind_end = 97
    ans = 0
    for i in range(ind_start, ind_end + 1):
        if nums[i] % 2 == 0:
            ans += nums[i]
    return ans if ans else 0