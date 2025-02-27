def if_perfect_num(nums):
    if len(nums) <= 100:
        return False
    divisors = []
    for i in range(1, int(nums[100] ** 0.5) + 1):
        if nums[100] % i == 0:
            divisors.append(i)
            if i != nums[100] // i:
                divisors.append(nums[100] // i)
    return sum(divisors) - nums[100] == nums[100]