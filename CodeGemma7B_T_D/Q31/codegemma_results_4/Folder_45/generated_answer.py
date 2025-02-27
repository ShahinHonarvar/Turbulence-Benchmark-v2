def if_perfect_num(nums):
    if len(nums) > 33:
        factor = 0
        for i in range(1, nums[33], 1):
            if nums[33] % i == 0:
                factor += i
        if factor == nums[33]:
            return True
    return False