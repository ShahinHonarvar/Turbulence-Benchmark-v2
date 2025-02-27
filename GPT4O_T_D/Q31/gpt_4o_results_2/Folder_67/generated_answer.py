def if_perfect_num(nums):
    if len(nums) > 43:
        n = nums[43]
        return n == sum((i for i in range(1, n) if n % i == 0))
    return False