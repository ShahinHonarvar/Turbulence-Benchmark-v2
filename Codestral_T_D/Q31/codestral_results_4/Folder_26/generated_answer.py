def if_perfect_num(nums):
    if len(nums) > 222:
        num = nums[222]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    return False