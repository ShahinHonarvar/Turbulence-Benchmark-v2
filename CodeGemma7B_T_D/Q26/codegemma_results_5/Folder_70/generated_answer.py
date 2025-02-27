def sum_in_range(nums):
    ans = 0
    for num in nums:
        if 408 <= num <= 495:
            ans += num
    return ans if ans else 0