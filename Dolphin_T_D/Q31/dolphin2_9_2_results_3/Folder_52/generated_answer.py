def if_perfect_num(nums):
    if len(nums) > 478:
        n = nums[478]
        return n == sum((1 for i in range(1, n) if n % i == 0))
    else:
        return False