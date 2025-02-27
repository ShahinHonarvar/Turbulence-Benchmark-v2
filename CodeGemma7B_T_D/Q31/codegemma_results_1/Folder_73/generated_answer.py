def if_perfect_num(nums):
    temp = nums[41]
    ans = 1 if temp == sum(range(1, temp)) else True if temp // 2 in range(1, temp) and (temp - 1) // 2 in range(1, temp) else False
    return ans