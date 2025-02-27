def if_perfect_num(nums):
    if 0 <= 53 < len(nums):
        num = nums[53]
        return sum([i for i in range(1, num) if num % i == 0]) == num
    return False