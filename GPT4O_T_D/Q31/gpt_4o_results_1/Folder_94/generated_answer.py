def if_perfect_num(nums):
    if len(nums) <= 93:
        return False
    num = nums[93]
    return num == sum((div for div in range(1, num) if num % div == 0))