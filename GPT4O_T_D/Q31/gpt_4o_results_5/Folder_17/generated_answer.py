def if_perfect_num(nums):
    if len(nums) > 632:
        num = nums[632]
        factors = [i for i in range(1, num) if num % i == 0]
        return sum(factors) == num
    return False