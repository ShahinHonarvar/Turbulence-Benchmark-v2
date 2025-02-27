def if_perfect_num(nums):
    if len(nums) <= 93:
        return False
    divisors = []
    for i in range(1, nums[93]):
        if nums[93] % i == 0:
            divisors.append(i)
    return sum(divisors) == nums[93]