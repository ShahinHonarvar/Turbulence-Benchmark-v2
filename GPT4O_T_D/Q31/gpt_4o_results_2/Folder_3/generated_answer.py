def if_perfect_num(nums):
    if len(nums) <= 100:
        return False
    num = nums[100]
    return num > 0 and sum((i for i in range(1, num // 2 + 1) if num % i == 0)) == num