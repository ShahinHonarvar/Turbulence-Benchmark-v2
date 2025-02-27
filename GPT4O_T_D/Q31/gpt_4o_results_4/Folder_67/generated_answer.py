def if_perfect_num(nums):
    if len(nums) > 43:
        num = nums[43]
        return sum((i for i in range(1, num) if num % i == 0)) == num
    return False