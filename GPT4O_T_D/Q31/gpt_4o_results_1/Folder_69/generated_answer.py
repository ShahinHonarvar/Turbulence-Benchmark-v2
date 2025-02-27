def if_perfect_num(nums):
    if nums[459] <= 0:
        return False
    divisors_sum = sum((i for i in range(1, nums[459]) if nums[459] % i == 0))
    return divisors_sum == nums[459]