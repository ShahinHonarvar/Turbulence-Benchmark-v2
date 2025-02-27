def if_perfect_num(nums):
    if len(nums) > 56:
        n = nums[56]
        return sum((i for i in range(1, n) if n % i == 0)) == n
    return False