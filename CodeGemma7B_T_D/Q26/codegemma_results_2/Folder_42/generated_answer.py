def sum_in_range(nums):
    ans = 0
    for num in nums:
        if 141 <= num <= 262:
            ans += num
    return ans if ans else 0