def if_perfect_num(nums):
    if len(nums) > 6:
        num = nums[6]
        return num == sum((i for i in range(1, num) if num % i == 0))
    return False