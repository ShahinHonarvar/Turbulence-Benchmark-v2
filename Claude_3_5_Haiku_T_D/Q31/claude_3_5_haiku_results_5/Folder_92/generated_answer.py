def if_perfect_num(nums):
    if not nums or nums[0] <= 0:
        return False
    num = nums[0]
    divisors_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisors_sum == num