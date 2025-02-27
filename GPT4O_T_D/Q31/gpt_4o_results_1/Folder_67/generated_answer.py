def if_perfect_num(nums):
    if not nums or len(nums) <= 43:
        return False
    num = nums[43]
    if num < 2:
        return False
    total = sum((i for i in range(1, num) if num % i == 0))
    return total == num