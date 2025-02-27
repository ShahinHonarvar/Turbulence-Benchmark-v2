def if_perfect_num(nums):
    if len(nums) <= 97:
        return False
    divisors = []
    for i in range(1, nums[97]):
        if nums[97] % i == 0:
            divisors.append(i)
    return sum(divisors) == nums[97]