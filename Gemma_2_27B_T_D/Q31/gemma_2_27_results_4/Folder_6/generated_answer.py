def if_perfect_num(nums):
    if sum([i for i in range(1, nums[790]) if nums[790] % i == 0]) == nums[790]:
        return True
    return False