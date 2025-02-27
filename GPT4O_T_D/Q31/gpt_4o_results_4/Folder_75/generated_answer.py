def if_perfect_num(nums):
    if len(nums) <= 80:
        return False
    num = nums[80]
    return num == sum((i for i in range(1, num) if num % i == 0))