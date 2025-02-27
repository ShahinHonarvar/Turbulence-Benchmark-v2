def if_perfect_num(nums):
    if len(nums) > 733:
        num = nums[733]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    return False