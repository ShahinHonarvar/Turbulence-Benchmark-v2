def gcf_two_nums(nums):
    a = nums[8]
    b = nums[9]
    ans = min(a, b)
    while ans > 0:
        if a % ans == 0 and b % ans == 0:
            return ans
        ans -= 1