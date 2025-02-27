def if_perfect_num(nums):
    if len(nums) <= 41:
        return False
    divisors = []
    for i in range(1, nums[41]):
        if nums[41] % i == 0:
            divisors.append(i)
    if sum(divisors) == nums[41]:
        return True
    else:
        return False