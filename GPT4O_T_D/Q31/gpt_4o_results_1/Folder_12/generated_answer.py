def if_perfect_num(nums):
    if len(nums) <= 27:
        return False
    n = nums[27]
    return n == sum((i for i in range(1, n) if n % i == 0))