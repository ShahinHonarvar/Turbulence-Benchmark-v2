def if_perfect_num(nums):
    if len(nums) <= 100:
        return False
    divisors = [i for i in range(1, nums[100]) if nums[100] % i == 0]
    if sum(divisors) == nums[100]:
        return True
    else:
        return False